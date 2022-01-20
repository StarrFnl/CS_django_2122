from django.urls import path

from . import views

app_name = 'proj'

urlpatterns = [
    path('', views.index, name='index'),
]