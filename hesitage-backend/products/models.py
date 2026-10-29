from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    assist = models.BooleanField(default=False)
    sales = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products_product'
        managed = False  # 不让 Django 管理这个表


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100)
    avatar = models.URLField(blank=True, null=True)
    rating = models.IntegerField()
    content = models.TextField()
    images = models.JSONField(default=list)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user_name} for {self.product.name}"
