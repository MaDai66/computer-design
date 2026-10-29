from django.db import migrations

def add_initial_tour_data(apps, schema_editor):
    Tour = apps.get_model('tours', 'Tour')
    TourDay = apps.get_model('tours', 'TourDay')
    TimeSlot = apps.get_model('tours', 'TimeSlot')
    HeritageHighlight = apps.get_model('tours', 'HeritageHighlight')
    CostInfo = apps.get_model('tours', 'CostInfo')
    TourReview = apps.get_model('tours', 'TourReview')
    
    # 1. 长白山满族寻根2日游
    tour1 = Tour.objects.create(
        name='长白山满族寻根2日游',
        description='探访满族发源地，体验传统手工艺，感受长白山自然美景。',
        image='/media/SmartTour/changbai_manchu.jpeg',
        duration='2',
        price=688,
        experience_points=3,
        rating=4.9,
        review_count=1280,
        sales_count=2580,
        tags=['满族文化', '长白山', '非遗体验']
    )
    
    day1 = TourDay.objects.create(tour=tour1, day_number=1, title='满族民俗村体验日')
    TimeSlot.objects.create(day=day1, time='08:00 - 09:00', activity='集合出发', description='指定地点集合，乘坐舒适旅游大巴前往满族民俗村')
    TimeSlot.objects.create(day=day1, time='09:00 - 11:30', activity='满族民俗村参观', description='游览满族传统建筑，了解满族历史文化')
    
    day2 = TourDay.objects.create(tour=tour1, day_number=2, title='长白山寻根日')
    TimeSlot.objects.create(day=day2, time='08:00 - 12:00', activity='长白山游览', description='参观长白山天池，欣赏壮丽的自然景观')
    
    HeritageHighlight.objects.create(tour=tour1, icon='🎨', title='满族剪纸', description='国家级非物质文化遗产，历史悠久')
    HeritageHighlight.objects.create(tour=tour1, icon='👘', title='满族传统服饰', description='色彩鲜艳，图案精美')
    
    CostInfo.objects.create(
        tour=tour1,
        includes=['全程旅游大巴交通', '1晚住宿', '3餐特色餐食', '景区门票', '所有非遗体验活动费用'],
        excludes=['个人消费', '往返集合地点的交通费用'],
        booking_notes=['至少提前3天预订', '人数限制：每团最多30人']
    )
    
    # 2. 朝鲜族民俗村1日游
    tour2 = Tour.objects.create(
        name='朝鲜族民俗村1日游',
        description='感受朝鲜族传统文化，品尝特色美食，体验传统手工艺。',
        image='/media/SmartTour/korean_village.jpeg',
        duration='1',
        price=298,
        experience_points=4,
        rating=4.8,
        review_count=2100,
        sales_count=4500,
        tags=['朝鲜族', '民俗体验', '美食之旅']
    )
    
    day_t2 = TourDay.objects.create(tour=tour2, day_number=1, title='朝鲜族民俗体验日')
    TimeSlot.objects.create(day=day_t2, time='08:00 - 09:00', activity='集合出发', description='前往朝鲜族民俗村')
    TimeSlot.objects.create(day=day_t2, time='09:30 - 12:00', activity='朝鲜族民俗村游览', description='参观朝鲜族传统村落，了解朝鲜族历史文化')
    TimeSlot.objects.create(day=day_t2, time='12:00 - 13:30', activity='朝鲜族特色午餐', description='品尝朝鲜族特色美食，如冷面、打糕等')
    TimeSlot.objects.create(day=day_t2, time='13:30 - 16:00', activity='打糕制作体验', description='学习制作朝鲜族打糕，体验传统手工艺')
    
    HeritageHighlight.objects.create(tour=tour2, icon='🥢', title='朝鲜族美食', description='朝鲜族特色美食，如冷面、打糕等')
    HeritageHighlight.objects.create(tour=tour2, icon='🎵', title='朝鲜族歌舞', description='欣赏朝鲜族传统歌舞表演')
    
    CostInfo.objects.create(
        tour=tour2,
        includes=['往返交通', '1餐特色午餐', '所有体验活动费用'],
        excludes=['个人消费'],
        booking_notes=['至少提前2天预订']
    )
    
    # 3. 查干湖冬捕3日游
    tour3 = Tour.objects.create(
        name='查干湖冬捕3日游',
        description='体验千年冬捕文化，感受北国风光，品尝新鲜湖鱼。',
        image='/media/SmartTour/chagan_winter.jpeg',
        duration='3',
        price=988,
        experience_points=2,
        rating=4.7,
        review_count=1850,
        sales_count=3200,
        tags=['冬捕', '查干湖', '冰雪世界']
    )
    
    day_t3_1 = TourDay.objects.create(tour=tour3, day_number=1, title='抵达查干湖')
    TimeSlot.objects.create(day=day_t3_1, time='08:00 - 12:00', activity='集合出发', description='前往查干湖')
    
    day_t3_2 = TourDay.objects.create(tour=tour3, day_number=2, title='冬捕体验')
    TimeSlot.objects.create(day=day_t3_2, time='06:00 - 10:00', activity='观看冬捕', description='观看千年冬捕技艺')
    
    day_t3_3 = TourDay.objects.create(tour=tour3, day_number=3, title='返程')
    TimeSlot.objects.create(day=day_t3_3, time='08:00 - 12:00', activity='返回市区', description='结束旅程')
    
    HeritageHighlight.objects.create(tour=tour3, icon='🎣', title='查干湖冬捕', description='千年冬捕技艺')
    HeritageHighlight.objects.create(tour=tour3, icon='🐟', title='湖鱼品尝', description='品尝查干湖新鲜鱼')
    
    CostInfo.objects.create(
        tour=tour3,
        includes=['往返交通', '2晚住宿', '5餐特色餐食', '冬捕体验'],
        excludes=['个人消费'],
        booking_notes=['至少提前5天预订']
    )
    
    # 4. 松花湖生态文化2日游
    tour4 = Tour.objects.create(
        name='松花湖生态文化2日游',
        description='游览松花湖美景，体验传统渔业文化，参与生态保护活动。',
        image='/media/SmartTour/songhua_ecological.jpeg',
        duration='2',
        price=588,
        experience_points=3,
        rating=4.6,
        review_count=1450,
        sales_count=2800,
        tags=['生态', '松花湖', '自然']
    )
    
    day_t4_1 = TourDay.objects.create(tour=tour4, day_number=1, title='松花湖游览')
    TimeSlot.objects.create(day=day_t4_1, time='08:00 - 12:00', activity='前往松花湖')
    
    day_t4_2 = TourDay.objects.create(tour=tour4, day_number=2, title='生态体验')
    TimeSlot.objects.create(day=day_t4_2, time='08:00 - 12:00', activity='生态保护活动', description='参与生态保护活动')
    
    HeritageHighlight.objects.create(tour=tour4, icon='🌿', title='生态保护', description='参与生态保护活动')
    HeritageHighlight.objects.create(tour=tour4, icon='🏞️', title='松花湖', description='游览松花湖美景')
    
    CostInfo.objects.create(
        tour=tour4,
        includes=['往返交通', '1晚住宿', '3餐特色餐食'],
        excludes=['个人消费'],
        booking_notes=['至少提前2天预订']
    )


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_remove_tour_route_tour_rating_tour_review_count_and_more'),
    ]

    operations = [
        migrations.RunPython(add_initial_tour_data),
    ]
