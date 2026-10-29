from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def minimal_test(request):
    if request.method == 'GET':
        return JsonResponse({'status': 'ok', 'message': 'Hello from tours API'})