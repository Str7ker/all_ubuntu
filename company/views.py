# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Company
#
# def index(request):
#     return HttpResponse("<h1>Компания</h1>")

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Company


# получение данных из бд
# def index(request):
#     people = Company.objects.all()
#     return render(request, "test.html", {"people": people})
#
# # # сохранение данных в бд
# # # def create(request):
# # #     if request.method == "POST":
# # #         tom = Company()
# # #         tom.name = request.POST.get("name")
# # #         tom.age = request.POST.get("age")
# # #         tom.save()
# # #     return HttpResponseRedirect("/")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from company.models import *
from company.serializers import *


class Companyes(APIView):
    """
    Компания
    """

    def get(self, request):
        company = Company.objects.all()
        serializer = CompanySerializers(company, many=True)
        return Response(serializer.data)


class Positions(APIView):
    """
    Должность
    """

    def get(self, request):
        position = Position.objects.all()
        serializer = PositionSerializers(position, many=True)
        return Response(serializer.data)


class Personals(APIView):
    """
    Должность
    """

    def get(self, request):
        personal = Personal.objects.all()
        serializer = PersonalSerializers(personal, many=True)
        return Response(serializer.data)


class Ratings(APIView):
    """
    Должность
    """

    def get(self, request):
        rating = Rating.objects.all()
        serializer = RatingSerializers(rating, many=True)
        return Response(serializer.data)
