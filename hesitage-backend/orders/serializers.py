from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product
from homestay.models import Homestay, HomestayRoom, HomestayExperience
from tours.models import Tour
from datetime import datetime
import uuid


class OrderItemSerializer(serializers.ModelSerializer):
    """订单明细序列化器"""

    class Meta:
        model = OrderItem
        fields = [
            'id', 'item_type', 'product_id', 'homestay_id', 'room_id',
            'experience_id', 'tour_id', 'name', 'image', 'price',
            'quantity', 'subtotal', 'specs', 'description'
        ]


class OrderItemCreateSerializer(serializers.Serializer):
    """创建订单项的数据验证"""
    item_type = serializers.ChoiceField(
        choices=['product', 'homestay', 'tour', 'experience'],
        required=True
    )
    item_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(default=1, min_value=1)

    def validate(self, attrs):
        """验证商品是否存在"""
        item_type = attrs['item_type']
        item_id = attrs['item_id']

        if item_type == 'product':
            if not Product.objects.filter(id=item_id).exists():
                raise serializers.ValidationError("商品不存在")
            product = Product.objects.get(id=item_id)
            attrs['name'] = product.name
            attrs['image'] = product.image
            attrs['price'] = product.price
            attrs['description'] = product.description

        elif item_type == 'homestay':
            if not Homestay.objects.filter(id=item_id).exists():
                raise serializers.ValidationError("乡宿不存在")
            homestay = Homestay.objects.get(id=item_id)
            attrs['name'] = homestay.name
            attrs['image'] = homestay.image
            attrs['price'] = homestay.price
            attrs['description'] = homestay.description

        elif item_type == 'tour':
            if not Tour.objects.filter(id=item_id).exists():
                raise serializers.ValidationError("旅游路线不存在")
            tour = Tour.objects.get(id=item_id)
            attrs['name'] = tour.name
            attrs['image'] = tour.image
            attrs['price'] = tour.price
            attrs['description'] = tour.description

        elif item_type == 'experience':
            if not HomestayExperience.objects.filter(id=item_id).exists():
                raise serializers.ValidationError("体验项目不存在")
            exp = HomestayExperience.objects.get(id=item_id)
            attrs['name'] = exp.name
            attrs['image'] = exp.image
            attrs['price'] = exp.price
            attrs['description'] = exp.description

        return attrs


class OrderSerializer(serializers.ModelSerializer):
    """订单序列化器"""
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    payment_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    # 添加关联商品的详细信息
    product_detail = serializers.SerializerMethodField()
    homestay_detail = serializers.SerializerMethodField()
    tour_detail = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id', 'order_id', 'user', 'type', 'type_display', 'status',
            'status_display', 'total_price', 'original_price', 'discount_amount',
            'contact_name', 'contact_phone', 'contact_address', 'notes',
            'check_in', 'check_out', 'travel_date', 'guests', 'nights',
            'payment_method', 'payment_time', 'items',
            'product_detail', 'homestay_detail', 'tour_detail',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'user', 'total_price', 'order_id', 'created_at', 'updated_at'
        ]

    def get_product_detail(self, obj):
        """获取商品详情"""
        items = obj.items.filter(item_type='product')
        if items.exists():
            details = []
            for item in items:
                try:
                    product = Product.objects.get(id=item.product_id)
                    details.append({
                        'id': product.id,
                        'name': product.name,
                        'image': product.image,
                        'price': str(product.price),
                        'category': product.category,
                        'assist': product.assist,
                        'sales': product.sales
                    })
                except Product.DoesNotExist:
                    pass
            return details
        return []

    def get_homestay_detail(self, obj):
        """获取乡宿详情"""
        items = obj.items.filter(item_type='homestay')
        if items.exists():
            details = []
            for item in items:
                try:
                    homestay = Homestay.objects.get(id=item.homestay_id)
                    details.append({
                        'id': homestay.id,
                        'name': homestay.name,
                        'image': homestay.image,
                        'price': str(homestay.price),
                        'location': homestay.location,
                        'rating': float(homestay.rating)
                    })
                except Homestay.DoesNotExist:
                    pass
            return details
        return []

    def get_tour_detail(self, obj):
        """获取旅游路线详情"""
        items = obj.items.filter(item_type='tour')
        if items.exists():
            details = []
            for item in items:
                try:
                    tour = Tour.objects.get(id=item.tour_id)
                    details.append({
                        'id': tour.id,
                        'name': tour.name,
                        'image': tour.image,
                        'price': str(tour.price),
                        'duration': tour.duration,
                        'rating': float(tour.rating)
                    })
                except Tour.DoesNotExist:
                    pass
            return details
        return []


class OrderCreateSerializer(serializers.ModelSerializer):
    """创建订单序列化器"""
    items = OrderItemCreateSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'type', 'contact_name', 'contact_phone', 'contact_address',
            'notes', 'check_in', 'check_out', 'travel_date', 'guests', 'nights',
            'items'
        ]

    def generate_order_id(self):
        """生成订单号"""
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        unique_id = str(uuid.uuid4())[:6].upper()
        return f"ORD{timestamp}{unique_id}"

    def create(self, validated_data):
        """创建订单"""
        items_data = validated_data.pop('items', [])

        # 生成订单号
        validated_data['order_id'] = self.generate_order_id()

        # 创建订单
        order = Order.objects.create(**validated_data)

        # 创建订单项
        total_price = 0
        for item_data in items_data:
            item_id = item_data.pop('item_id')
            item_type = item_data['item_type']

            # 根据类型设置关联ID
            item_data['order'] = order
            item_data['item_type'] = item_type

            if item_type == 'product':
                item_data['product_id'] = item_id
            elif item_type == 'homestay':
                item_data['homestay_id'] = item_id
            elif item_type == 'tour':
                item_data['tour_id'] = item_id
            elif item_type == 'experience':
                item_data['experience_id'] = item_id

            order_item = OrderItem.objects.create(**item_data)
            total_price += order_item.subtotal

        # 更新订单总价
        order.total_price = total_price
        order.save()

        return order


class OrderListSerializer(serializers.ModelSerializer):
    """订单列表序列化器（简化版）"""
    user = serializers.StringRelatedField(read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    items_count = serializers.SerializerMethodField()
    first_item_name = serializers.SerializerMethodField()
    first_item_image = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'order_id', 'user', 'type', 'type_display', 'status',
            'status_display', 'total_price', 'items_count', 'first_item_name',
            'first_item_image', 'contact_name', 'contact_phone', 'created_at'
        ]

    def get_items_count(self, obj):
        """获取商品数量"""
        return obj.items.count()

    def get_first_item_name(self, obj):
        """获取第一个商品名称"""
        first_item = obj.items.first()
        return first_item.name if first_item else ''

    def get_first_item_image(self, obj):
        """获取第一个商品图片"""
        first_item = obj.items.first()
        return first_item.image if first_item else ''


class OrderStatusUpdateSerializer(serializers.Serializer):
    """订单状态更新序列化器"""
    status = serializers.ChoiceField(choices=Order.ORDER_STATUS)
    notes = serializers.CharField(required=False, allow_blank=True)


class OrderStatisticsSerializer(serializers.Serializer):
    """订单统计序列化器"""
    total_orders = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=10, decimal_places=2)
    pending_orders = serializers.IntegerField()
    paid_orders = serializers.IntegerField()
    completed_orders = serializers.IntegerField()
    cancelled_orders = serializers.IntegerField()
    product_orders = serializers.IntegerField()
    homestay_orders = serializers.IntegerField()
    tour_orders = serializers.IntegerField()
    experience_orders = serializers.IntegerField()
