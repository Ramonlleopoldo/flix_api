import json
from django.views.decorators.csrf import csrf_exempt
from genres.models import GenresModel
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

@csrf_exempt
def genre_created_list_view(request):
    if request.method == 'GET':
        genres = GenresModel.objects.all()
        data = [{'id':genre.id,'name':genre.name}for genre in genres]
        return JsonResponse(data,safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = GenresModel(name = data['name'])
        new_genre.save()
        return JsonResponse({'id':new_genre.id , 'name':new_genre.name}, status=201 )
@csrf_exempt  
def genre_detail_view(request, pk):
    genre = get_object_or_404(GenresModel,pk=pk)
    if request.method == 'GET':
        data = {'id':genre.id, 'name':genre.name}
        return JsonResponse(data)
    elif request.method == 'PUT' :
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse({'id':genre.id , 'name':genre.name})
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'id':genre.id, 'name':genre.name, 'status':'excluido'}, status = 204)
        