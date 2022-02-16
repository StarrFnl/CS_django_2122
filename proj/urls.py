from django.urls import path, include
from django.contrib import admin

from . import views



app_name = 'proj'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('<int:post_normal_id>/', views.detail_normal, name='detail_normal'),
    path('post_normal/create/', views.post_normal_create, name='create_normal'),
    path('post_normal/delete/<int:post_normal_id>/', views.post_normal_delete, name='post_normal_delete'),
]