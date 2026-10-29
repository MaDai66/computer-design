from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def debug_test(request):
    if request.method == 'GET':
        try:
            from tours.models import Tour
            # Check model fields
            fields = [f.name for f in Tour._meta.fields]
            return JsonResponse({
                'model_fields': fields,
                'has_image_base64': 'image_base64' in fields,
                'has_gallery_base64': 'gallery_base64' in fields
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)