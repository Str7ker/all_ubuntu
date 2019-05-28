from rest_framework import serializers
from personalarea.models import *


class NewPersonalSerializers(serializers.ModelSerializer):
    """
    Сериализация компании
    """

    class Meta:
        model = New_personal
        fields = '__all__'


class PersonalareaSerializers(serializers.ModelSerializer):
    """
    Сериализация должности
    """

    class Meta:
        model = Personalarea
        fields = '__all__'
