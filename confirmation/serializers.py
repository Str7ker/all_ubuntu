from rest_framework import serializers
from confirmation.models import *


class ConfirmationSerializers(serializers.ModelSerializer):
    """
    Сериализация подтверждения
    """

    class Meta:
        model = Confirmation
        fields = '__all__'


