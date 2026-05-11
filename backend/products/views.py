from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
from .models import Product

# Create your views here.
@csrf_exempt
def product_list(request):
    if request.method == 'GET':
        # 获取查询参数
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        category = request.GET.get('category', None)
        
        # 构建查询集
        products = Product.objects.all()
        
        # 按类别筛选
        if category:
            products = products.filter(category=category)
        
        # 分页
        paginator = Paginator(products, limit)
        page_obj = paginator.get_page(page)
        
        # 构建响应数据
        results = []
        for product in page_obj.object_list:
            results.append({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': float(product.price),
                'category': product.category,
                'origin': product.origin,
                'stock': product.stock,
                'created_at': product.created_at.isoformat(),
                'image': product.image.url if product.image else None
            })
        
        return JsonResponse({
            'results': results,
            'total_pages': paginator.num_pages,
            'current_page': page_obj.number
        })
    elif request.method == 'POST':
        # 创建产品
        try:
            data = json.loads(request.body)
            product = Product.objects.create(
                name=data.get('name'),
                description=data.get('description'),
                price=data.get('price'),
                category=data.get('category'),
                origin=data.get('origin'),
                stock=data.get('stock')
            )
            return JsonResponse({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': float(product.price),
                'category': product.category,
                'origin': product.origin,
                'stock': product.stock,
                'created_at': product.created_at.isoformat()
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price),
            'category': product.category,
            'origin': product.origin,
            'stock': product.stock,
            'created_at': product.created_at.isoformat(),
            'image': product.image.url if product.image else None
        })
    elif request.method == 'PUT':
        # 更新产品
        try:
            data = json.loads(request.body)
            product.name = data.get('name', product.name)
            product.description = data.get('description', product.description)
            product.price = data.get('price', product.price)
            product.category = data.get('category', product.category)
            product.origin = data.get('origin', product.origin)
            product.stock = data.get('stock', product.stock)
            product.save()
            return JsonResponse({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': float(product.price),
                'category': product.category,
                'origin': product.origin,
                'stock': product.stock,
                'created_at': product.created_at.isoformat()
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    elif request.method == 'DELETE':
        # 删除产品
        product.delete()
        return JsonResponse({'success': True}, status=204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def agricultural_products(request):
    # 获取农产品
    products = Product.objects.filter(category='agricultural')
    results = []
    for product in products:
        results.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price),
            'origin': product.origin,
            'stock': product.stock,
            'image': product.image.url if product.image else None
        })
    return JsonResponse({'results': results})
