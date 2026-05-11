from django.http import JsonResponse

# Create your views here.
def homestay_list(request):
    return JsonResponse({'message': 'Homestay list endpoint'})

def homestay_detail(request, id):
    return JsonResponse({'message': f'Homestay detail endpoint for ID {id}'})

def homestay_experience(request):
    return JsonResponse({'message': 'Homestay experience endpoint'})
