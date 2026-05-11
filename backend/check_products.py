import os
import django

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

# 导入Product模型
from products.models import Product

# 检查产品数量
product_count = Product.objects.count()
print(f'产品数量: {product_count}')

# 打印产品列表
print('产品列表:')
for product in Product.objects.all():
    print(f'ID: {product.id}, 名称: {product.name}, 价格: {product.price}')

# 如果没有产品，创建一些示例数据
if product_count == 0:
    print('\n数据库中没有产品，创建示例数据...')
    
    # 创建示例产品
    products = [
        {
            'name': '满族剪纸艺术套装',
            'description': '满族剪纸是中国非物质文化遗产，历史悠久，风格独特。本套装包含剪纸工具、材料和教程，让您在家就能体验满族剪纸的魅力。',
            'price': 128.0,
            'stock': 500,
            'origin': '吉林省',
            'image': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Manchu%20paper%20cutting%20art%20traditional%20craft%20Jilin&image_size=portrait_4_3'
        },
        {
            'name': '长白山野生人参',
            'description': '地道长白山特产，营养丰富，品质上乘。',
            'price': 298.0,
            'stock': 200,
            'origin': '吉林省长白山',
            'image': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Changbai%20Mountain%20wild%20ginseng%20Jilin&image_size=portrait_4_3'
        },
        {
            'name': '吉林有机玉米',
            'description': '无污染有机种植，口感香甜，营养丰富。',
            'price': 39.9,
            'stock': 1000,
            'origin': '吉林省',
            'image': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Jilin%20organic%20corn%20agricultural%20products&image_size=portrait_4_3'
        }
    ]
    
    for product_data in products:
        product = Product(**product_data)
        product.save()
        print(f'创建产品: {product.name}')
    
    print('\n创建完成！现在产品数量:', Product.objects.count())