from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import PostNormal

def index(request):
    return render(request, 'base.html') #나중에 proj/main.html로 변경해야함

def list(request):
    return render(request, 'proj/list.html')