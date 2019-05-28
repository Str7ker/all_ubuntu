from rest_framework import serializers
from cargos.models import *


class CargosSerializers(serializers.ModelSerializer):
    """
    Сериализация грузов
    """

    class Meta:
        model = Cargos
        fields = '__all__'

