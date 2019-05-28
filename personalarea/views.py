# from django.http import HttpResponse
#
#
# def personal(request):
#     return HttpResponse("Персонал")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from personalarea.models import *
from personalarea.serializers import *


class NewPersonal(APIView):
    """
    Новый персонал
    """

    def get(self, request):
        company = New_personal.objects.all()
        serializer = NewPersonalSerializers(company, many=True)
        return Response(serializer.data)


class Personalareas(APIView):
    """
    Персонал
    """

    def get(self, request):
        position = Personalarea.objects.all()
        serializer = PersonalareaSerializers(position, many=True)
        return Response(serializer.data)

