from django.db import models
from users.models import User
from decimal import Decimal


class Order(models.Model):
    """订单主表"""
    ORDER_STATUS = [
        ('pending', '待付款'),
        ('paid', '已付款'),
        ('confirmed', '已确认'),
        ('completed', '已完成'),
        ('cancelled', '已取消'),
        ('refunded', '已退款')
    ]

    ORDER_TYPES = [
        ('product', '商品订单'),
        ('homestay', '民宿订单'),
        ('tour', '旅游路线订单'),
        ('experience', '体验项目订单')
    ]

    # 用户信息
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders',
        verbose_name='用户'
    )

    # 订单基本信息
    order_id = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='订单号'
    )
    type = models.CharField(
        max_length=20,
        choices=ORDER_TYPES,
        default='product',
        verbose_name='订单类型'
    )
    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS,
        default='pending',
        verbose_name='订单状态'
    )

    # 金额信息
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name='订单总价'
    )
    original_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name='原价'
    )
    discount_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal('0.00'),
        verbose_name='优惠金额'
    )

    # 联系人信息
    contact_name = models.CharField(
        max_length=100,
        blank=True,
        default='',
        verbose_name='联系人姓名'
    )
    contact_phone = models.CharField(
        max_length=20,
        blank=True,
        default='',
        verbose_name='联系电话'
    )
    contact_address = models.CharField(
        max_length=500,
        blank=True,
        default='',
        verbose_name='收货地址'
    )

    # 订单备注
    notes = models.TextField(
        blank=True,
        default='',
        verbose_name='订单备注'
    )

    # 时间相关字段
    check_in = models.DateField(
        null=True,
        blank=True,
        verbose_name='入住日期'
    )
    check_out = models.DateField(
        null=True,
        blank=True,
        verbose_name='离店日期'
    )
    travel_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='出行日期'
    )
    guests = models.IntegerField(
        default=1,
        verbose_name='入住人数'
    )
    nights = models.IntegerField(
        default=1,
        verbose_name='入住晚数'
    )

    # 支付信息
    payment_method = models.CharField(
        max_length=50,
        blank=True,
        default='',
        verbose_name='支付方式'
    )
    payment_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='支付时间'
    )

    # 时间戳
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新时间'
    )

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'
        ordering = ['-created_at']

    def __str__(self):
        return f"订单 {self.order_id} - {self.get_type_display()}"

    def calculate_total(self):
        """计算订单总价"""
        items = self.items.all()
        total = sum(item.price * item.quantity for item in items)
        self.total_price = total
        return total


class OrderItem(models.Model):
    """订单明细表"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='订单'
    )

    # 商品/服务类型
    item_type = models.CharField(
        max_length=20,
        choices=[
            ('product', '商品'),
            ('homestay', '乡宿'),
            ('tour', '旅游路线'),
            ('experience', '体验项目')
        ],
        default='product',
        verbose_name='商品类型'
    )

    # 关联的商品ID
    product_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='商品ID'
    )
    homestay_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='乡宿ID'
    )
    room_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='房型ID'
    )
    experience_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='体验项目ID'
    )
    tour_id = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='路线ID'
    )

    # 商品信息快照
    name = models.CharField(
        max_length=255,
        verbose_name='商品名称'
    )
    image = models.CharField(
        max_length=500,
        blank=True,
        default='',
        verbose_name='商品图片'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='单价'
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name='数量'
    )
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='小计'
    )

    # 规格信息（JSON格式）
    specs = models.JSONField(
        null=True,
        blank=True,
        verbose_name='规格参数'
    )

    # 描述
    description = models.TextField(
        blank=True,
        default='',
        verbose_name='商品描述'
    )

    class Meta:
        verbose_name = '订单明细'
        verbose_name_plural = '订单明细'

    def __str__(self):
        return f"{self.name} x {self.quantity}"

    def save(self, *args, **kwargs):
        """保存时自动计算小计"""
        self.subtotal = self.price * self.quantity
        super().save(*args, **kwargs)
