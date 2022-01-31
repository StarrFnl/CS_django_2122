from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post_Normal
from .forms import Post_Normal_Form


# Create your views here.

def index(request):
    return render(request, 'titlep/titlep.html') #나중에 proj/main.html로 변경해야함

def list(request):
    post_normal_list = Post_Normal.objects.order_by('-create_date')
    context = {'post_normal_list': post_normal_list}
    return render(request, 'proj/list.html', context)


def post_normal_create(request):
    if request.method == 'POST':
        form = Post_Normal_Form(request.POST, request.FILES)
        if form.is_valid():
            post_normal = form.save(commit=False)
            post_normal.create_date = timezone.now()
            post_normal.save()
            return redirect('proj:list')
    else:
        form = Post_Normal_Form()
    context = {'form': form}
    return render(request, 'proj/post_normal_create.html', context)



def detail_normal(request, post_normal_id):
    """
    pybo 내용 출력
    """
    post_normal = Post_Normal.objects.get(id=post_normal_id)
    context = {'post_normal': post_normal}
    return render(request, 'detailp/detail_main.html', context)
