import json
from django.views.decorators.csrf import csrf_exempt
from genres.models import GenresModel
from django.http import JsonResponse

@csrf_exempt
def genres_list_view(request):
    if request.method == 'GET':
        genres = GenresModel.objects.all()
        data = [{'id':genre.id,'name':genre.name}for genre in genres]
        return JsonResponse(data,safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = GenresModel(name = data['name'])
        new_genre.save()
        return JsonResponse({'id':new_genre.id , 'name':new_genre.name}, status=201 )
        
