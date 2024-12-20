from django.core.management.base import BaseCommand
from actors.models import ActorsModel


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('nome_ator', type=str, help='Digite o nome do ator')
        parser.add_argument('nacionalidade', type=str, help='Digite a nacionalidade')

    def handle(self, *arg, **options):
        new_actor = options['nome_ator']
        new_acotor_nationality = options['nacionalidade']
        ActorsModel.objects.create(name=new_actor, nationality=new_acotor_nationality)
        print(f"Ator: {new_actor} Nacionalidade: {new_acotor_nationality} Cadastrado com sucesso.")
