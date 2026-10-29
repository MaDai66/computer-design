from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, ProductReview
from .serializers import ProductSerializer, ProductReviewSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        if category:
            if category == '助农专区':
                queryset = queryset.filter(assist=True)
            else:
                queryset = queryset.filter(category=category)
        return queryset
    
    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        product = self.get_object()
        reviews = ProductReview.objects.filter(product=product)
        serializer = ProductReviewSerializer(reviews, many=True)
        return Response(serializer.data)