from rest_framework import serializers
from actors.models import ActorsModel


class ActorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActorsModel
        fields = '__all__'
