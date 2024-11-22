from genres.models import GenresModel
from django.http import JsonResponse

def genres_list_view(request):
    genres = GenresModel.objects.all()
    data = [{'id':genre.id,'name':genre.name}for genre in genres]
    return JsonResponse(data,safe=False)
