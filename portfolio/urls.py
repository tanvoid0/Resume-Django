from django.contrib import admin
from django.urls import path, include

from . import  views

app_name = 'portfolio'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.test, name='index'),

]
