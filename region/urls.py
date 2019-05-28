"""region URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from company import views
#
# urlpatterns = [
#     path('', views.index, name='company'),
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from company import views
from django.contrib import admin
from django.urls import path
from company.views import *
from cargos.views import *
from confirmation.views import *
from personalarea.views import *
urlpatterns = [
    # path('', views.index, name='home'),
    # path('company/', TemplateView.as_view(template_name='company.html', extra_context={"header": "О сайте"}),
    #      name='company'),
    # path('admin/', admin.site.urls),
    path('', Companyes.as_view()),
    path('position/', Positions.as_view()),
    path('personal/', Personals.as_view()),
    path('rating/', Ratings.as_view()),
    path('cargos/', Cargoes.as_view()),
    path('conf/', Confirmations.as_view()),
    path('newpersonal/', NewPersonal.as_view()),
    path('personalarea/', Personalareas.as_view()),
    path('admin/', admin.site.urls),
]
