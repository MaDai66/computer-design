from django.db import migrations

def add_homestay_data(apps, schema_editor):
    Homestay = apps.get_model('homestay', 'Homestay')
    
    homestays_data = [
        {
            'name': '长白山脚下农家院',
            'description': '位于长白山脚下，环境优美，提供满族剪纸体验，正宗农家菜。',
            'image': '/media/homestay/372127531b22cf3b11b561b712ab9aae.jpeg',
            'images': [],
            'price': 280.00,
            'rating': 4.8,
            'review_count': 156,
            'location': '长白山景区附近',
            'distance': 5,
            'area': 'changbai',
            'has_heritage': True,
            'self_operated': True,
            'hot': True,
            'facilities': ['kang', 'wifi', 'bathroom', 'parking', 'restaurant']
        },
        {
            'name': '松花湖生态农家院',
            'description': '松花湖边的生态农家院，提供传统渔业体验，湖景房。',
            'image': '/media/homestay/5e722f3174856920f5a95763187cfabe.jpeg',
            'images': [],
            'price': 320.00,
            'rating': 4.6,
            'review_count': 89,
            'location': '松花湖景区',
            'distance': 10,
            'area': 'songhua',
            'has_heritage': True,
            'self_operated': True,
            'hot': False,
            'facilities': ['wifi', 'bathroom', 'parking', 'restaurant']
        },
        {
            'name': '朝鲜族民俗村农家院',
            'description': '朝鲜族特色农家院，提供打糕制作、朝鲜服装体验，正宗朝鲜美食。',
            'image': '/media/homestay/fb02a59c68ee0050700468e4f137cc0d.jpeg',
            'images': [],
            'price': 260.00,
            'rating': 4.9,
            'review_count': 234,
            'location': '朝鲜族民俗村',
            'distance': 15,
            'area': 'korean',
            'has_heritage': True,
            'self_operated': True,
            'hot': True,
            'facilities': ['kang', 'wifi', 'bathroom', 'parking', 'restaurant']
        },
        {
            'name': '查干湖冬捕农家院',
            'description': '查干湖边的农家院，冬季提供冬捕体验，特色鱼宴。',
            'image': '/media/homestay/87d003eb75a414662e86f3c2231ba9b4.jpeg',
            'images': [],
            'price': 300.00,
            'rating': 4.7,
            'review_count': 178,
            'location': '查干湖景区',
            'distance': 20,
            'area': 'chagan',
            'has_heritage': True,
            'self_operated': True,
            'hot': True,
            'facilities': ['kang', 'wifi', 'bathroom', 'parking', 'restaurant']
        }
    ]
    
    for data in homestays_data:
        Homestay.objects.update_or_create(
            name=data['name'],
            defaults=data
        )

class Migration(migrations.Migration):

    dependencies = [
        ('homestay', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_homestay_data),
    ]