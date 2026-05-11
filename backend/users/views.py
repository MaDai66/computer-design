from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import base64
from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from .models import User

# Create your views here.

@csrf_exempt
@require_http_methods(['POST'])
def register(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username or not email or not password:
            return JsonResponse({'error': 'Missing required fields'}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        return JsonResponse({'message': 'Registration successful', 'user_id': user.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return JsonResponse({
                'token': 'mock-token',  # 实际项目中应该返回真实的JWT token
                'username': user.username,
                'role': 'admin' if user.is_staff else 'user'
            })
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def profile(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Not authenticated'}, status=401)
        
        user = request.user
        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'phone': user.phone,
            'bio': user.bio,
            'avatar': user.avatar.url if user.avatar else None
        })
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Not authenticated'}, status=401)
        
        try:
            data = json.loads(request.body)
            user = request.user
            
            if 'username' in data:
                user.username = data['username']
            if 'email' in data:
                user.email = data['email']
            if 'phone' in data:
                user.phone = data['phone']
            if 'bio' in data:
                user.bio = data['bio']
            if 'avatar' in data and data['avatar']:
                # 处理base64编码的头像
                avatar_data = data['avatar']
                if avatar_data.startswith('data:image/'):
                    try:
                        # 提取base64数据
                        format, imgstr = avatar_data.split(';base64,')
                        ext = format.split('/')[-1]
                        # 检查文件扩展名
                        if ext not in ['jpg', 'jpeg', 'png', 'gif']:
                            return JsonResponse({'error': 'Unsupported image format'}, status=400)
                        # 创建ContentFile对象
                        avatar_file = ContentFile(base64.b64decode(imgstr), name=f'avatar.{ext}')
                        user.avatar = avatar_file
                    except Exception as e:
                        return JsonResponse({'error': f'Avatar processing error: {str(e)}'}, status=400)
            
            user.save()
            
            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'phone': user.phone,
                'bio': user.bio,
                'avatar': user.avatar.url if user.avatar else None
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        # 获取查询参数
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)
        
        # 构建查询集
        users = User.objects.all()
        
        # 分页
        paginator = Paginator(users, limit)
        page_obj = paginator.get_page(page)
        
        # 构建响应数据
        results = []
        for user in page_obj.object_list:
            results.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'phone': user.phone,
                'avatar': user.avatar.url if user.avatar else None,
                'is_active': user.is_active,
                'is_staff': user.is_staff,
                'date_joined': user.date_joined.isoformat(),
                'last_login': user.last_login.isoformat() if user.last_login else None
            })
        
        return JsonResponse({
            'results': results,
            'total_pages': paginator.num_pages,
            'current_page': page_obj.number
        })
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def user_detail(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'phone': user.phone,
            'bio': user.bio,
            'avatar': user.avatar.url if user.avatar else None,
            'is_active': user.is_active,
            'is_staff': user.is_staff,
            'date_joined': user.date_joined.isoformat(),
            'last_login': user.last_login.isoformat() if user.last_login else None
        })
    elif request.method == 'PUT':
        # 更新用户
        try:
            data = json.loads(request.body)
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.phone = data.get('phone', user.phone)
            user.bio = data.get('bio', user.bio)
            user.is_active = data.get('is_active', user.is_active)
            user.is_staff = data.get('is_staff', user.is_staff)
            user.save()
            return JsonResponse({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'phone': user.phone,
                'bio': user.bio,
                'avatar': user.avatar.url if user.avatar else None,
                'is_active': user.is_active,
                'is_staff': user.is_staff
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    elif request.method == 'DELETE':
        # 删除用户
        user.delete()
        return JsonResponse({'success': True}, status=204)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def toggle_user_status(request, id):
    try:
        user = User.objects.get(id=id)
        user.is_active = not user.is_active
        user.save()
        return JsonResponse({
            'success': True,
            'is_active': user.is_active
        })
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
