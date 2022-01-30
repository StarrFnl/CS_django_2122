from django.urls import path
from django.contrib import admin

from . import views

# 이미지 업로드용
from django.conf.urls.static import static
from django.conf import settings

app_name = 'proj'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('<int:post_normal_id>/', views.detail_normal, name='detail_normal'),
    path('post_normal/create/', views.post_normal_create, name='create_normal')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)