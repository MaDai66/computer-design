from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tour

@csrf_exempt
def simple_tour_list(request):
    if request.method == 'GET':
        try:
            tours = Tour.objects.all()
            results = []
            for tour in tours:
                results.append({
                    'id': tour.id,
                    'name': tour.name,
                    'has_image': bool(tour.image_base64),
                })
            return JsonResponse({'results': results})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)