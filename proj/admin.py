from django.contrib import admin
from .models import PostNormal

# Register your models here.
class PostNormalAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(PostNormal, PostNormalAdmin)