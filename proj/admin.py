from django.contrib import admin
from .models import Post_Normal

# Register your models here.
class Post_NormalAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Post_Normal, Post_NormalAdmin)

