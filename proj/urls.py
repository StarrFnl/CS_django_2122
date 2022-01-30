from django.urls import path
from django.contrib import admin

from . import views

app_name = 'proj'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
]