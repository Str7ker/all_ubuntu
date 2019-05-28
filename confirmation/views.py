from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from confirmation.models import *
from confirmation.serializers import *


class Confirmations(APIView):
    """
    Компания
    """

    def get(self, request):
        confirmation = Confirmation.objects.all()
        serializer = ConfirmationSerializers(confirmation, many=True)
        return Response(serializer.data)