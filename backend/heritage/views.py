from django.http import JsonResponse

# Create your views here.
def heritage_list(request):
    return JsonResponse({'message': 'Heritage list endpoint'})

def heritage_detail(request, id):
    return JsonResponse({'message': f'Heritage detail endpoint for ID {id}'})

def heritage_experience(request):
    return JsonResponse({'message': 'Heritage experience endpoint'})
