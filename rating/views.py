from django.http import HttpResponse


def rating(request):
    return HttpResponse("Рейтинг")