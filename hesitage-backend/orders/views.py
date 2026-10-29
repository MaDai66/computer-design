from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta

from .models import Order, OrderItem
from .serializers import (
    OrderSerializer, OrderListSerializer, OrderCreateSerializer,
    OrderStatusUpdateSerializer, OrderStatisticsSerializer
)


def get_user_from_request(request):
    """从请求中获取用户对象"""
    # 优先使用已认证用户
    if request.user.is_authenticated:
        return request.user

    # 如果未认证，尝试从请求头获取用户ID
    user_id = request.headers.get('X-User-Id')

    # 也尝试从请求体获取 user_id
    if not user_id and hasattr(request, 'data') and isinstance(request.data, dict):
        user_id = request.data.get('user_id')

    if user_id:
        from users.models import User
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            pass

    return None


class OrderViewSet(viewsets.ModelViewSet):
    """订单视图集"""
    queryset = Order.objects.all()
    permission_classes = [AllowAny]  # 允许所有用户访问，方便测试

    def get_serializer_class(self):
        """根据操作类型返回不同的序列化器"""
        if self.action == 'create':
            return OrderCreateSerializer
        elif self.action == 'list':
            return OrderListSerializer
        elif self.action == 'retrieve':
            return OrderSerializer
        return OrderSerializer

    def get_queryset(self):
        """获取查询集"""
        queryset = Order.objects.all().prefetch_related('items')

        # 根据用户筛选
        user = self.request.query_params.get('user')
        if user:
            queryset = queryset.filter(user_id=user)

        # 根据状态筛选
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)

        # 根据类型筛选
        type_filter = self.request.query_params.get('type')
        if type_filter:
            queryset = queryset.filter(type=type_filter)

        # 根据时间范围筛选
        date_from = self.request.query_params.get('date_from')
        if date_from:
            queryset = queryset.filter(created_at__gte=date_from)

        date_to = self.request.query_params.get('date_to')
        if date_to:
            queryset = queryset.filter(created_at__lte=date_to)

        # 根据订单号搜索
        order_id = self.request.query_params.get('order_id')
        if order_id:
            queryset = queryset.filter(order_id__icontains=order_id)

        # 根据联系人姓名搜索
        contact_name = self.request.query_params.get('contact_name')
        if contact_name:
            queryset = queryset.filter(contact_name__icontains=contact_name)

        # 根据联系电话搜索
        contact_phone = self.request.query_params.get('contact_phone')
        if contact_phone:
            queryset = queryset.filter(contact_phone__icontains=contact_phone)

        return queryset.order_by('-created_at')

    def create(self, request, *args, **kwargs):
        """创建订单"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 创建订单并关联用户
        order = serializer.save()
        
        # 关联用户（支持多种认证方式）
        user = get_user_from_request(request)
        if user:
            order.user = user
            order.save()

        # 返回完整订单信息
        response_serializer = OrderSerializer(order)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        """更新订单状态"""
        order = self.get_object()
        serializer = OrderStatusUpdateSerializer(data=request.data)

        if serializer.is_valid():
            old_status = order.status
            new_status = serializer.validated_data['status']
            order.status = new_status

            if 'notes' in serializer.validated_data:
                order.notes = serializer.validated_data['notes']

            # 如果是支付操作，记录支付时间
            if new_status == 'paid' and old_status == 'pending':
                order.payment_time = timezone.now()
                order.payment_method = request.data.get('payment_method', 'online')

            order.save()

            return Response({
                'message': '订单状态更新成功',
                'order_id': order.order_id,
                'old_status': old_status,
                'new_status': new_status,
                'updated_at': order.updated_at
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """取消订单"""
        order = self.get_object()

        if order.status in ['completed', 'cancelled', 'refunded']:
            return Response({
                'message': '当前订单状态无法取消'
            }, status=status.HTTP_400_BAD_REQUEST)

        order.status = 'cancelled'
        order.notes = request.data.get('reason', '用户取消')
        order.save()

        return Response({
            'message': '订单取消成功',
            'order_id': order.order_id
        })

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        """获取订单详细信息"""
        order = self.get_object()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """获取订单统计信息"""
        queryset = self.get_queryset()

        # 基本统计
        total_orders = queryset.count()
        total_revenue = queryset.filter(
            status__in=['paid', 'confirmed', 'completed']
        ).aggregate(total=Sum('total_price'))['total'] or 0

        # 按状态统计
        pending_orders = queryset.filter(status='pending').count()
        paid_orders = queryset.filter(status='paid').count()
        completed_orders = queryset.filter(status='completed').count()
        cancelled_orders = queryset.filter(status='cancelled').count()

        # 按类型统计
        product_orders = queryset.filter(type='product').count()
        homestay_orders = queryset.filter(type='homestay').count()
        tour_orders = queryset.filter(type='tour').count()
        experience_orders = queryset.filter(type='experience').count()

        # 今日统计
        today = timezone.now().date()
        today_orders = queryset.filter(
            created_at__date=today
        ).count()
        today_revenue = queryset.filter(
            status__in=['paid', 'confirmed', 'completed'],
            created_at__date=today
        ).aggregate(total=Sum('total_price'))['total'] or 0

        # 本周统计
        week_start = today - timedelta(days=today.weekday())
        week_orders = queryset.filter(
            created_at__date__gte=week_start
        ).count()
        week_revenue = queryset.filter(
            status__in=['paid', 'confirmed', 'completed'],
            created_at__date__gte=week_start
        ).aggregate(total=Sum('total_price'))['total'] or 0

        # 本月统计
        month_start = today.replace(day=1)
        month_orders = queryset.filter(
            created_at__date__gte=month_start
        ).count()
        month_revenue = queryset.filter(
            status__in=['paid', 'confirmed', 'completed'],
            created_at__date__gte=month_start
        ).aggregate(total=Sum('total_price'))['total'] or 0

        data = {
            'total_orders': total_orders,
            'total_revenue': float(total_revenue),
            'pending_orders': pending_orders,
            'paid_orders': paid_orders,
            'completed_orders': completed_orders,
            'cancelled_orders': cancelled_orders,
            'product_orders': product_orders,
            'homestay_orders': homestay_orders,
            'tour_orders': tour_orders,
            'experience_orders': experience_orders,
            'today_orders': today_orders,
            'today_revenue': float(today_revenue),
            'week_orders': week_orders,
            'week_revenue': float(week_revenue),
            'month_orders': month_orders,
            'month_revenue': float(month_revenue)
        }

        return Response(data)

    @action(detail=False, methods=['get'])
    def my_orders(self, request):
        """获取当前用户的订单（支持多种查询方式）"""
        # 方式1：如果用户已认证，直接返回用户订单
        if request.user.is_authenticated:
            orders = Order.objects.filter(user=request.user).prefetch_related('items')
            serializer = OrderListSerializer(orders, many=True)
            return Response(serializer.data)
        
        # 方式2：通过请求头获取用户ID
        user_id = request.headers.get('X-User-Id')
        if user_id:
            from users.models import User
            try:
                user = User.objects.get(id=user_id)
                orders = Order.objects.filter(user=user).prefetch_related('items')
                serializer = OrderListSerializer(orders, many=True)
                return Response(serializer.data)
            except User.DoesNotExist:
                pass
        
        # 方式3：通过查询参数获取用户ID
        user_id_param = request.query_params.get('user_id')
        if user_id_param:
            from users.models import User
            try:
                user = User.objects.get(id=user_id_param)
                orders = Order.objects.filter(user=user).prefetch_related('items')
                serializer = OrderListSerializer(orders, many=True)
                return Response(serializer.data)
            except User.DoesNotExist:
                pass
        
        # 方式4：通过查询参数方式
        order_id = request.query_params.get('order_id')
        contact_phone = request.query_params.get('contact_phone')
        
        # 方式5：请求头方式（便于前端传递）
        if not contact_phone:
            contact_phone = request.headers.get('X-Contact-Phone')
        
        if order_id:
            orders = Order.objects.filter(order_id__icontains=order_id).prefetch_related('items')
            serializer = OrderListSerializer(orders, many=True)
            return Response(serializer.data)
        
        if contact_phone:
            orders = Order.objects.filter(contact_phone=contact_phone).prefetch_related('items')
            serializer = OrderListSerializer(orders, many=True)
            return Response(serializer.data)
        
        # 如果没有提供任何查询条件，返回空列表
        return Response([])

    @action(detail=False, methods=['post'])
    def create_product_order(self, request):
        """创建商品订单（简化版）"""
        product_id = request.data.get('product_id')
        quantity = max(int(request.data.get('quantity', 1)), 1)
        contact_name = request.data.get('contact_name', '')
        contact_phone = request.data.get('contact_phone', '')
        contact_address = request.data.get('contact_address', '')
        notes = request.data.get('notes', '')

        from products.models import Product
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({
                'message': '商品不存在'
            }, status=status.HTTP_404_NOT_FOUND)

        # 创建订单
        from .serializers import OrderCreateSerializer
        data = {
            'type': 'product',
            'contact_name': contact_name,
            'contact_phone': contact_phone,
            'contact_address': contact_address,
            'notes': notes,
            'items': [{
                'item_type': 'product',
                'item_id': product_id,
                'quantity': quantity
            }]
        }

        serializer = OrderCreateSerializer(data=data)
        if not serializer.is_valid():
            print('Product order validation errors:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        order = serializer.save()

        # 关联用户（支持多种认证方式）
        user = get_user_from_request(request)
        if user:
            order.user = user
            order.save()

        response_serializer = OrderSerializer(order)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def create_homestay_order(self, request):
        """创建民宿订单（简化版）"""
        homestay_id = request.data.get('homestay_id')
        room_id = request.data.get('room_id')
        check_in = request.data.get('check_in')
        check_out = request.data.get('check_out')
        guests = request.data.get('guests', 1)
        contact_name = request.data.get('contact_name', '')
        contact_phone = request.data.get('contact_phone', '')
        notes = request.data.get('notes', '')

        from homestay.models import Homestay, HomestayRoom
        try:
            homestay = Homestay.objects.get(id=homestay_id)
        except Homestay.DoesNotExist:
            return Response({
                'message': '民宿不存在'
            }, status=status.HTTP_404_NOT_FOUND)

        room = None
        if room_id:
            try:
                room = HomestayRoom.objects.get(id=room_id, homestay=homestay)
            except HomestayRoom.DoesNotExist:
                return Response({
                    'message': '房型不存在'
                }, status=status.HTTP_404_NOT_FOUND)

        # 计算晚数（至少1晚）
        from datetime import datetime
        if check_in and check_out:
            d1 = datetime.strptime(str(check_in), '%Y-%m-%d')
            d2 = datetime.strptime(str(check_out), '%Y-%m-%d')
            nights = max((d2 - d1).days, 1)
        else:
            nights = 1

        # 创建订单
        data = {
            'type': 'homestay',
            'contact_name': contact_name,
            'contact_phone': contact_phone,
            'notes': notes,
            'check_in': check_in,
            'check_out': check_out,
            'guests': guests,
            'nights': nights,
            'items': [{
                'item_type': 'homestay',
                'item_id': homestay_id,
                'quantity': nights
            }]
        }

        serializer = OrderCreateSerializer(data=data)
        if not serializer.is_valid():
            print('Homestay order validation errors:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        order = serializer.save()

        # 关联用户（支持多种认证方式）
        user = get_user_from_request(request)
        if user:
            order.user = user
            order.save()

        response_serializer = OrderSerializer(order)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def create_tour_order(self, request):
        """创建旅游路线订单（简化版）"""
        import logging
        logger = logging.getLogger(__name__)
        
        tour_id = request.data.get('tour_id')
        travel_date = request.data.get('travel_date')
        guests = max(int(request.data.get('guests', 1)), 1)
        contact_name = request.data.get('contact_name', '')
        contact_phone = request.data.get('contact_phone', '')
        notes = request.data.get('notes', '')

        logger.info(f"创建旅游订单: tour_id={tour_id}, guests={guests}, contact_name={contact_name}")
        logger.info(f"用户认证状态: {request.user.is_authenticated}")
        if request.user.is_authenticated:
            logger.info(f"当前用户: {request.user.id} - {request.user.username}")

        from tours.models import Tour
        try:
            tour = Tour.objects.get(id=tour_id)
        except Tour.DoesNotExist:
            logger.error(f"旅游路线不存在: tour_id={tour_id}")
            return Response({
                'message': '旅游路线不存在'
            }, status=status.HTTP_404_NOT_FOUND)

        # 创建订单
        data = {
            'type': 'tour',
            'contact_name': contact_name,
            'contact_phone': contact_phone,
            'notes': notes,
            'travel_date': travel_date,
            'guests': guests,
            'items': [{
                'item_type': 'tour',
                'item_id': tour_id,
                'quantity': guests
            }]
        }

        serializer = OrderCreateSerializer(data=data)
        if serializer.is_valid():
            order = serializer.save()
            
            # 关联用户（支持多种认证方式）
            user = get_user_from_request(request)
            if user:
                order.user = user
                order.save()
                logger.info(f"订单关联用户成功: order_id={order.order_id}, user_id={user.id}")
            else:
                logger.warning(f"订单未关联用户: order_id={order.order_id}")

            response_serializer = OrderSerializer(order)
            logger.info(f"订单创建成功: order_id={order.order_id}")
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"订单验证失败: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def create_experience_order(self, request):
        """创建体验项目订单（简化版）"""
        experience_id = request.data.get('experience_id')
        # 兼容前端不同的字段名：guests / participants
        guests = request.data.get('guests', request.data.get('participants', 1))
        # 兼容前端不同的字段名：travel_date / date
        travel_date = request.data.get('travel_date', request.data.get('date'))
        contact_name = request.data.get('contact_name', '')
        contact_phone = request.data.get('contact_phone', '')
        notes = request.data.get('notes', '')

        from homestay.models import HomestayExperience
        try:
            experience = HomestayExperience.objects.get(id=experience_id)
        except HomestayExperience.DoesNotExist:
            return Response({
                'message': '体验项目不存在'
            }, status=status.HTTP_404_NOT_FOUND)

        # 确保参与人数至少为1
        guests = max(int(guests), 1)

        # 创建订单
        data = {
            'type': 'experience',
            'contact_name': contact_name,
            'contact_phone': contact_phone,
            'notes': notes,
            'travel_date': travel_date,
            'guests': guests,
            'items': [{
                'item_type': 'experience',
                'item_id': experience_id,
                'quantity': guests
            }]
        }

        serializer = OrderCreateSerializer(data=data)
        if not serializer.is_valid():
            print('Experience order validation errors:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        order = serializer.save()

        user = get_user_from_request(request)
        if user:
            order.user = user
            order.save()

        response_serializer = OrderSerializer(order)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
