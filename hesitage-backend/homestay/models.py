from django.db import models


class Homestay(models.Model):
    """乡宿核心信息"""
    AREA_CHOICES = [
        ('changbai', '长白山'),
        ('songhua', '松花湖'),
        ('chagan', '查干湖'),
        ('korean', '朝鲜族民俗村'),
        ('other', '其他'),
    ]

    name = models.CharField(max_length=255, verbose_name='乡宿名称')
    description = models.TextField(verbose_name='乡宿描述')
    image = models.CharField(max_length=500, blank=True, null=True, verbose_name='封面图')
    images = models.JSONField(default=list, blank=True, verbose_name='图片列表')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='起价/晚')

    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, verbose_name='评分')
    review_count = models.IntegerField(default=0, verbose_name='评价数')

    location = models.CharField(max_length=255, verbose_name='位置')
    distance = models.IntegerField(default=0, verbose_name='距离景区(km)')

    area = models.CharField(max_length=20, choices=AREA_CHOICES, default='other', verbose_name='所在区域')

    # 标签
    has_heritage = models.BooleanField(default=False, verbose_name='有非遗体验')
    self_operated = models.BooleanField(default=True, verbose_name='农家自营')
    hot = models.BooleanField(default=False, verbose_name='热销')

    # 设施（JSON格式存储）
    facilities = models.JSONField(default=list, blank=True, verbose_name='设施列表')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '乡宿'
        verbose_name_plural = '乡宿'
        ordering = ['-created_at']


class HomestayRoom(models.Model):
    """房型信息"""
    homestay = models.ForeignKey(Homestay, on_delete=models.CASCADE, related_name='rooms')

    name = models.CharField(max_length=255, verbose_name='房型名称')
    image = models.CharField(max_length=500, blank=True, null=True, verbose_name='房型图片')
    description = models.TextField(blank=True, verbose_name='房型描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格/晚')
    capacity = models.CharField(max_length=50, verbose_name='容纳人数')

    def __str__(self):
        return f'{self.homestay.name} - {self.name}'

    class Meta:
        verbose_name = '房型'
        verbose_name_plural = '房型'


class HomestayExperience(models.Model):
    """非遗体验项目"""
    homestay = models.ForeignKey(Homestay, on_delete=models.CASCADE, related_name='experiences')

    name = models.CharField(max_length=255, verbose_name='体验项目名称')
    image = models.CharField(max_length=500, blank=True, null=True, verbose_name='体验图片')
    description = models.TextField(blank=True, verbose_name='体验描述')
    duration = models.CharField(max_length=100, verbose_name='时长')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格/人')

    def __str__(self):
        return f'{self.homestay.name} - {self.name}'

    class Meta:
        verbose_name = '体验项目'
        verbose_name_plural = '体验项目'


class HomestayReview(models.Model):
    """乡宿评价"""
    homestay = models.ForeignKey(Homestay, on_delete=models.CASCADE, related_name='reviews')

    user_name = models.CharField(max_length=100, verbose_name='用户名')
    avatar = models.CharField(max_length=500, blank=True, null=True, verbose_name='用户头像')
    rating = models.IntegerField(default=5, verbose_name='评分')
    content = models.TextField(verbose_name='评价内容')
    date = models.DateField(auto_now_add=True, verbose_name='评价日期')

    def __str__(self):
        return f'{self.user_name} - {self.homestay.name}'

    class Meta:
        verbose_name = '乡宿评价'
        verbose_name_plural = '乡宿评价'
        ordering = ['-date']
