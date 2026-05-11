from django.http import JsonResponse

# Create your views here.
def activity_list(request):
    return JsonResponse({'message': 'Activity list endpoint'})

def activity_detail(request, id):
    return JsonResponse({'message': f'Activity detail endpoint for ID {id}'})

def upcoming_activities(request):
    return JsonResponse({'message': 'Upcoming activities endpoint'})
