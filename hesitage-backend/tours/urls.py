from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TourViewSet, TourDayViewSet, TimeSlotViewSet,
    HeritageHighlightViewSet, CostInfoViewSet, TourReviewViewSet,
    get_tour_reviews
)

router = DefaultRouter()
# 先注册具体的子路由，再注册主路由
router.register(r'days', TourDayViewSet, basename='tour-day')
router.register(r'time-slots', TimeSlotViewSet, basename='time-slot')
router.register(r'highlights', HeritageHighlightViewSet, basename='highlight')
router.register(r'cost-info', CostInfoViewSet, basename='cost-info')
router.register(r'reviews', TourReviewViewSet, basename='tour-review')
router.register(r'', TourViewSet, basename='tour')  # 空路径放在最后

urlpatterns = [
    path('', include(router.urls)),
    # 添加嵌套路由：获取特定tour的评论
    path('<int:tour_id>/reviews/', get_tour_reviews, name='tour-specific-reviews'),
]