from django.db import models

# Create your models here.

class PostNormal(models.Model):
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    subject = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)