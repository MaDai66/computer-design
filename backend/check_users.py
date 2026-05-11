import os
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

# 导入User模型
from users.models import User

# 查询所有用户
users = User.objects.all()
print('用户数量:', users.count())

# 打印每个用户的信息
for user in users:
    print(f'用户名: {user.username}, 邮箱: {user.email}, 密码: {user.password}')
