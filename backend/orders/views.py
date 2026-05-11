from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
from .models import Order

@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        # 获取查询参数
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        status = request.GET.get('status', None)
        
        # 构建查询集
        orders = Order.objects.all().order_by('-created_at')
        
        # 按状态筛选
        if status:
            orders = orders.filter(status=status)
        
        # 分页
        paginator = Paginator(orders, limit)
        page_obj = paginator.get_page(page)
        
        # 构建响应数据
        results = []
        for order in page_obj.object_list:
            results.append({
                'id': order.order_id,
                'user': order.user.username if order.user else '未知用户',
                'item': order.item,
                'amount': float(order.total_price),
                'itemsCount': order.quantity,
                'status': order.status,
                'statusText': order.status,
                'createTime': order.created_at.isoformat(),
                'checkIn': order.check_in.isoformat() if order.check_in else None,
                'checkOut': order.check_out.isoformat() if order.check_out else None,
                'date': order.date.isoformat() if order.date else None,
                'time': order.time.isoformat() if order.time else None,
                'spec': order.spec,
                'guests': order.guests,
                'participants': order.participants
            })
        
        return JsonResponse({
            'results': results,
            'total_pages': paginator.num_pages,
            'current_page': page_obj.number
        })
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def order_detail(request, order_id):
    try:
        order = Order.objects.get(order_id=order_id)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'id': order.order_id,
            'user': order.user.username if order.user else '未知用户',
            'item': order.item,
            'price': float(order.price),
            'quantity': order.quantity,
            'amount': float(order.total_price),
            'status': order.status,
            'statusText': order.status,
            'createTime': order.created_at.isoformat(),
            'checkIn': order.check_in.isoformat() if order.check_in else None,
            'checkOut': order.check_out.isoformat() if order.check_out else None,
            'date': order.date.isoformat() if order.date else None,
            'time': order.time.isoformat() if order.time else None,
            'spec': order.spec,
            'guests': order.guests,
            'participants': order.participants
        })
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_order_status(request, order_id):
    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            order = Order.objects.get(order_id=order_id)
            order.status = data.get('status', order.status)
            order.save()
            return JsonResponse({
                'success': True,
                'order_id': order.order_id,
                'status': order.status
            })
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_order(request, order_id):
    if request.method == 'DELETE':
        try:
            order = Order.objects.get(order_id=order_id)
            order.delete()
            return JsonResponse({'success': True, 'message': 'Order deleted successfully'})
        except Order.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Order not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # 验证必填字段
            required_fields = ['order_id', 'item', 'price', 'total_price']
            for field in required_fields:
                if not data.get(field):
                    return JsonResponse({'success': False, 'error': f'Missing required field: {field}'}, status=400)
            
            # 获取当前登录用户
            user = request.user if request.user.is_authenticated else None
            
            order = Order.objects.create(
                user=user,
                order_id=data.get('order_id'),
                item=data.get('item'),
                price=data.get('price'),
                quantity=data.get('quantity', 1),
                total_price=data.get('total_price'),
                status=data.get('status', '待付款'),
                check_in=data.get('check_in'),
                check_out=data.get('check_out'),
                date=data.get('date'),
                time=data.get('time'),
                spec=data.get('spec'),
                guests=data.get('guests'),
                participants=data.get('participants')
            )
            return JsonResponse({'success': True, 'order_id': order.order_id})
        except json.JSONDecodeError as e:
            return JsonResponse({'success': False, 'error': 'Invalid JSON format'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
