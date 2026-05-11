from django.http import JsonResponse

# Create your views here.
def community_list(request):
    return JsonResponse({'message': 'Community list endpoint'})

def community_detail(request, id):
    return JsonResponse({'message': f'Community detail endpoint for ID {id}'})

def travel_note(request):
    return JsonResponse({'message': 'Travel note endpoint'})
