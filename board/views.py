from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator
# form.py에서 가져옴
from .form import BlogPost

def home(request):
    return render(request, 'home.html')

def board(request):
    blogs = Blog.objects #쿼리셋
    # 블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    # request된 페이지를 얻어온 뒤 return 해 준다.
    posts = paginator.get_page(page)
    return render(request, 'board.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    blog = Blog()
    return render(request, 'detail.html', {'blog':blog, 'details': details})

def new(request):
    return render(request, 'new.html')

# 약식으로 작성한것 본격정
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/board/detail/' + str(blog.id))

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # DB에 저장하지 않고 form에 임시 저장
            # 나머지 안 쓴거 쓰기
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')     # 바로 home으로 redirect
    
    # 2. 빈 페이지를 띄어주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form}) # form형태로 전달

# 삭제하기
def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('board')

# 수정하기