from django.db import models
from users.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    order_id = models.CharField(max_length=100, unique=True)
    item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='待付款')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 额外字段，用于不同类型的订单
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    spec = models.JSONField(null=True, blank=True)
    guests = models.IntegerField(null=True, blank=True)
    participants = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Order {self.order_id} - {self.item}"
