from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from cargos.models import *
from cargos.serializers import *


class Cargoes(APIView):
    """
    Грузы
    """

    def get(self, request):
        cargo = Cargos.objects.all()
        serializer = CargosSerializers(cargo, many=True)
        return Response(serializer.data)

