from django.contrib import admin
from .models import Post_Normal, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

# Register your models here.
class Post_NormalAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    inlines = [PhotoInline, ]


admin.site.register(Post_Normal, Post_NormalAdmin)





