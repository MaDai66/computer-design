from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tour

@csrf_exempt
def test_tour_api(request):
    try:
        tour = Tour.objects.get(id=8)
        return JsonResponse({
            'name': tour.name,
            'image_exists': bool(tour.image_base64),
            'gallery_count': len(tour.gallery_base64) if tour.gallery_base64 else 0
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)