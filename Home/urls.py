from django.contrib import admin
from django.urls import path, include

from . import  views


urlpatterns = [
    path('', views.index, name='index'),
    path('cv', views.cv, name='cv'),
    path('test', views.test, name='test'),
    path('weditor', views.weditor, name='weditor'),

]
