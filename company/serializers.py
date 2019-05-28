from rest_framework import serializers
from company.models import *


class CompanySerializers(serializers.ModelSerializer):
    """
    Сериализация компании
    """

    class Meta:
        model = Company
        fields = '__all__'


class PositionSerializers(serializers.ModelSerializer):
    """
    Сериализация должности
    """

    class Meta:
        model = Position
        fields = '__all__'


class PersonalSerializers(serializers.ModelSerializer):
    """
    Сериализация персонала
    """

    class Meta:
        model = Personal
        fields = '__all__'


class RatingSerializers(serializers.ModelSerializer):
    """
    Сериализация рейтинга
    """

    class Meta:
        model = Rating
        fields = '__all__'
