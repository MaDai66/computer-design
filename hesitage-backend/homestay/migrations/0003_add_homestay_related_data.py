from django.db import migrations

def add_homestay_related_data(apps, schema_editor):
    Homestay = apps.get_model('homestay', 'Homestay')
    HomestayRoom = apps.get_model('homestay', 'HomestayRoom')
    HomestayExperience = apps.get_model('homestay', 'HomestayExperience')
    HomestayReview = apps.get_model('homestay', 'HomestayReview')
    
    # 长白山脚下农家院
    changbai = Homestay.objects.filter(name='长白山脚下农家院').first()
    if changbai:
        # 房间
        rooms_changbai = [
            {
                'name': '火炕房',
                'image': '/media/homestay/room_kang.jpeg',
                'description': '传统火炕，可住2-4人，独立卫浴，空调，WiFi',
                'price': 280.00,
                'capacity': '2-4人'
            },
            {
                'name': '山景房',
                'image': '/media/homestay/room_mountain.jpeg',
                'description': '落地窗山景，可住2人，独立卫浴，空调，WiFi',
                'price': 320.00,
                'capacity': '2人'
            },
            {
                'name': '家庭房',
                'image': '/media/homestay/room_family.jpeg',
                'description': '宽敞空间，可住4-6人，独立卫浴，空调，WiFi',
                'price': 480.00,
                'capacity': '4-6人'
            }
        ]
        
        for room_data in rooms_changbai:
            HomestayRoom.objects.update_or_create(
                homestay=changbai,
                name=room_data['name'],
                defaults=room_data
            )
        
        # 体验项目
        experiences_changbai = [
            {
                'name': '满族剪纸教学',
                'image': '/media/homestay/exp_papercutting.jpeg',
                'description': '由当地非遗传承人教授满族传统剪纸技艺，可带走自己的作品。',
                'duration': '1.5小时',
                'price': 68.00
            },
            {
                'name': '满族火锅体验',
                'image': '/media/homestay/exp_hotpot.jpeg',
                'description': '品尝正宗满族火锅，了解满族饮食文化和传统烹饪方法。',
                'duration': '2小时',
                'price': 128.00
            }
        ]
        
        for exp_data in experiences_changbai:
            HomestayExperience.objects.update_or_create(
                homestay=changbai,
                name=exp_data['name'],
                defaults=exp_data
            )
        
        # 评价
        reviews_changbai = [
            {
                'user_name': '@旅行爱好者',
                'avatar': '/media/homestay/avatar_1.jpeg',
                'rating': 5,
                'content': '农家院环境非常好，干净整洁，老板热情好客。火炕很舒服，晚上睡得很香。早餐是正宗的农家菜，味道很棒。离长白山景区很近，交通方便。强烈推荐！'
            },
            {
                'user_name': '@家庭出游',
                'avatar': '/media/homestay/avatar_2.jpeg',
                'rating': 5,
                'content': '带家人来长白山旅游，选择了这家农家院。房间宽敞，设施齐全，孩子们很喜欢火炕。老板还安排了满族剪纸体验，非常有特色。下次来还会住这里。'
            },
            {
                'user_name': '@摄影爱好者',
                'avatar': '/media/homestay/avatar_3.jpeg',
                'rating': 5,
                'content': '农家院的位置绝佳，是拍摄长白山的好地方。房间干净舒适，老板很热情，给我们推荐了很多拍摄点。晚上在院子里还能看到星空，非常美丽。'
            }
        ]
        
        for review_data in reviews_changbai:
            HomestayReview.objects.update_or_create(
                homestay=changbai,
                user_name=review_data['user_name'],
                content=review_data['content'][:250],
                defaults=review_data
            )
    
    # 松花湖生态农家院
    songhua = Homestay.objects.filter(name='松花湖生态农家院').first()
    if songhua:
        # 房间
        rooms_songhua = [
            {
                'name': '湖景房',
                'image': '/media/homestay/room_lake.jpeg',
                'description': '落地窗湖景，可住2-3人，独立卫浴，空调，WiFi',
                'price': 320.00,
                'capacity': '2-3人'
            },
            {
                'name': '家庭湖景房',
                'image': '/media/homestay/room_family_lake.jpeg',
                'description': '宽敞湖景，可住4-5人，独立卫浴，空调，WiFi',
                'price': 450.00,
                'capacity': '4-5人'
            }
        ]
        
        for room_data in rooms_songhua:
            HomestayRoom.objects.update_or_create(
                homestay=songhua,
                name=room_data['name'],
                defaults=room_data
            )
        
        # 体验项目
        experiences_songhua = [
            {
                'name': '传统渔业体验',
                'image': '/media/homestay/exp_fishing.jpeg',
                'description': '跟随当地渔民学习传统捕鱼技艺，体验撒网、收网的乐趣。',
                'duration': '2小时',
                'price': 88.00
            },
            {
                'name': '湖鲜烹饪体验',
                'image': '/media/homestay/exp_cooking.jpeg',
                'description': '使用刚捕获的湖鲜，学习制作正宗的松花湖鱼宴。',
                'duration': '1.5小时',
                'price': 108.00
            }
        ]
        
        for exp_data in experiences_songhua:
            HomestayExperience.objects.update_or_create(
                homestay=songhua,
                name=exp_data['name'],
                defaults=exp_data
            )
        
        # 评价
        reviews_songhua = [
            {
                'user_name': '@自然爱好者',
                'avatar': '/media/homestay/avatar_4.jpeg',
                'rating': 5,
                'content': '农家院环境非常生态，周围都是绿色植物，空气清新。房间宽敞明亮，湖景房的视野非常好。老板很热情，给我们安排了捕鱼体验，非常有趣。'
            },
            {
                'user_name': '@美食家',
                'avatar': '/media/homestay/avatar_5.jpeg',
                'rating': 4,
                'content': '湖鲜非常新鲜，味道很棒。房间干净整洁，设施齐全。唯一的不足是离市区有点远，但环境确实很好，适合度假。'
            }
        ]
        
        for review_data in reviews_songhua:
            HomestayReview.objects.update_or_create(
                homestay=songhua,
                user_name=review_data['user_name'],
                content=review_data['content'][:250],
                defaults=review_data
            )
    
    # 朝鲜族民俗村农家院
    korean = Homestay.objects.filter(name='朝鲜族民俗村农家院').first()
    if korean:
        # 房间
        rooms_korean = [
            {
                'name': '韩式火炕房',
                'image': '/media/homestay/room_korean_ondol.jpeg',
                'description': '传统韩式火炕，可住2-4人，独立卫浴，空调，WiFi',
                'price': 260.00,
                'capacity': '2-4人'
            },
            {
                'name': '韩式客房',
                'image': '/media/homestay/room_korean_guest.jpeg',
                'description': '韩式风格客房，可住2人，独立卫浴，空调，WiFi',
                'price': 280.00,
                'capacity': '2人'
            }
        ]
        
        for room_data in rooms_korean:
            HomestayRoom.objects.update_or_create(
                homestay=korean,
                name=room_data['name'],
                defaults=room_data
            )
        
        # 体验项目
        experiences_korean = [
            {
                'name': '打糕制作体验',
                'image': '/media/homestay/exp_ricecake.jpeg',
                'description': '学习制作正宗朝鲜族打糕，体验传统捣糕工艺。',
                'duration': '1小时',
                'price': 58.00
            },
            {
                'name': '朝鲜服装体验',
                'image': '/media/homestay/exp_clothing.jpeg',
                'description': '穿上正宗朝鲜服装，在民俗村拍照留念。',
                'duration': '1.5小时',
                'price': 68.00
            },
            {
                'name': '朝鲜美食制作',
                'image': '/media/homestay/exp_korean_cuisine.jpeg',
                'description': '学习制作正宗朝鲜泡菜、烤肉等传统美食。',
                'duration': '2小时',
                'price': 98.00
            }
        ]
        
        for exp_data in experiences_korean:
            HomestayExperience.objects.update_or_create(
                homestay=korean,
                name=exp_data['name'],
                defaults=exp_data
            )
        
        # 评价
        reviews_korean = [
            {
                'user_name': '@文化爱好者',
                'avatar': '/media/homestay/avatar_6.jpeg',
                'rating': 5,
                'content': '非常有特色的朝鲜族农家院，老板是朝鲜族，非常热情。打糕制作体验很有趣，味道也很棒。房间干净整洁，朝鲜风格很地道。强烈推荐！'
            },
            {
                'user_name': '@摄影爱好者',
                'avatar': '/media/homestay/avatar_7.jpeg',
                'rating': 5,
                'content': '民俗村的环境非常适合拍照，穿上朝鲜服装拍出来的照片非常漂亮。农家院的饭菜很正宗，尤其是泡菜和烤肉。房间舒适，服务周到。'
            },
            {
                'user_name': '@家庭出游',
                'avatar': '/media/homestay/avatar_8.jpeg',
                'rating': 5,
                'content': '孩子们非常喜欢打糕制作和朝鲜服装体验，玩得很开心。农家院的环境干净整洁，饭菜味道好。老板很热情，还给我们讲了很多朝鲜族的文化和历史。'
            }
        ]
        
        for review_data in reviews_korean:
            HomestayReview.objects.update_or_create(
                homestay=korean,
                user_name=review_data['user_name'],
                content=review_data['content'][:250],
                defaults=review_data
            )
    
    # 查干湖冬捕农家院
    chagan = Homestay.objects.filter(name='查干湖冬捕农家院').first()
    if chagan:
        # 房间
        rooms_chagan = [
            {
                'name': '暖炕房',
                'image': '/media/homestay/room_warm_kang.jpeg',
                'description': '传统暖炕，可住2-4人，独立卫浴，暖气，WiFi',
                'price': 300.00,
                'capacity': '2-4人'
            },
            {
                'name': '豪华暖炕房',
                'image': '/media/homestay/room_deluxe_warm.jpeg',
                'description': '宽敞暖炕，可住4-6人，独立卫浴，暖气，WiFi',
                'price': 420.00,
                'capacity': '4-6人'
            }
        ]
        
        for room_data in rooms_chagan:
            HomestayRoom.objects.update_or_create(
                homestay=chagan,
                name=room_data['name'],
                defaults=room_data
            )
        
        # 体验项目
        experiences_chagan = [
            {
                'name': '冬捕体验',
                'image': '/media/homestay/exp_winter_fishing.jpeg',
                'description': '参与查干湖传统冬捕，体验冰上捕鱼的乐趣。',
                'duration': '3小时',
                'price': 168.00
            },
            {
                'name': '鱼宴品尝',
                'image': '/media/homestay/exp_fish_feast.jpeg',
                'description': '品尝查干湖特色鱼宴，包括多种做法的鲜鱼。',
                'duration': '2小时',
                'price': 138.00
            }
        ]
        
        for exp_data in experiences_chagan:
            HomestayExperience.objects.update_or_create(
                homestay=chagan,
                name=exp_data['name'],
                defaults=exp_data
            )
        
        # 评价
        reviews_chagan = [
            {
                'user_name': '@冬季旅游爱好者',
                'avatar': '/media/homestay/avatar_9.jpeg',
                'rating': 5,
                'content': '冬捕体验非常棒，第一次在冰面上捕鱼，非常新鲜刺激。农家院的暖炕很舒服，晚上睡在上面很暖和。鱼宴的味道非常鲜美，推荐大家来体验。'
            },
            {
                'user_name': '@美食爱好者',
                'avatar': '/media/homestay/avatar_10.jpeg',
                'rating': 4,
                'content': '鱼宴非常美味，特别是查干湖的胖头鱼，肉质鲜嫩。冬捕体验很有趣，但需要注意保暖。农家院的环境干净整洁，服务周到。'
            }
        ]
        
        for review_data in reviews_chagan:
            HomestayReview.objects.update_or_create(
                homestay=chagan,
                user_name=review_data['user_name'],
                content=review_data['content'][:250],
                defaults=review_data
            )

class Migration(migrations.Migration):

    dependencies = [
        ('homestay', '0002_add_homestay_data'),
    ]

    operations = [
        migrations.RunPython(add_homestay_related_data),
    ]