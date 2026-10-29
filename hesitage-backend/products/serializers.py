from rest_framework import serializers
from .models import Product, ProductReview


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['id', 'user_name', 'avatar', 'rating', 'content', 'images', 'date']


class ProductSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'price', 'original_price', 
                  'discount', 'category', 'reviews', 'created_at', 'assist', 'sales']