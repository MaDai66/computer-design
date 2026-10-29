from django.contrib import admin
from .models import Product, ProductReview


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'sales', 'assist']
    list_filter = ['category', 'assist']
    search_fields = ['name']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'product', 'rating', 'date']
    list_filter = ['rating', 'date']
