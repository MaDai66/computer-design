from django.http import JsonResponse

# Create your views here.
def tour_list(request):
    return JsonResponse({'message': 'Tour list endpoint'})

def tour_detail(request, id):
    return JsonResponse({'message': f'Tour detail endpoint for ID {id}'})

def tour_route(request):
    return JsonResponse({'message': 'Tour route endpoint'})
