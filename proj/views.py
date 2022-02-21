from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post_Normal, Photo
from .forms import Post_Normal_Form
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    return render(request, 'titlep/titlep.html') #나중에 proj/main.html로 변경해야함

def list(request):
    page = request.GET.get('page', '1')

    post_normal_list = Post_Normal.objects.order_by('-create_date')
    paginator = Paginator(post_normal_list, 10)
    max_page = len(paginator.page_range)
    page_obj = paginator.get_page(page)

    context = {'post_normal_list': page_obj, 'max_page': max_page}
    return render(request, 'proj/list.html', context)


def post_normal_create(request):
    if request.method == 'POST':
        form = Post_Normal_Form(request.POST, request.FILES)
        if form.is_valid():
            post_normal = form.save(commit=False)
            post_normal.create_date = timezone.now()
            post_normal.save()
            for img in request.FILES.getlist('images'):
                photo = Photo()
                photo.post_n = post_normal
                photo.images = img
                photo.save()
            return redirect('proj:list')
    else:
        form = Post_Normal_Form()
    context = {'form': form}
    return render(request, 'proj/post_normal_create.html', context)



def detail_normal(request, post_normal_id):
    """
    proj 내용 출력
    """
    post_normal = Post_Normal.objects.get(id=post_normal_id)
    context = {'post_normal': post_normal}
    return render(request, 'detailp/detail_main.html', context)


@login_required(login_url='common:login')
def post_normal_delete(request, post_normal_id):
    """
    proj 질문삭제
    """
    post_normal = get_object_or_404(Post_Normal, pk=post_normal_id)
    # if request.user != post_normal.author:
    #     messages.error(request, '삭제권한이 없습니다')
    #     return redirect('proj:detail', post_normal_id=post_normal.id)
    post_normal.delete()
    return redirect('proj:list')
