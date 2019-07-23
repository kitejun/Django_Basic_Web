from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 파일 저장 import문
from django.core.files.storage import FileSystemStorage

from .models import Board
from .form import BoardPost

def home(request):
    return render(request, 'home.html')

def board(request):
    boards = Board.objects #쿼리셋
    # 블로그 모든 글들을 대상으로
    board_list = Board.objects.all()
    # 블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(board_list, 3)
    # request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')

    try:
    # request된 페이지를 얻어온 뒤 return 해 준다.
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'board.html', {'boards':boards, 'posts':posts})

def detail(request, board_id):
    details = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'details': details})


def new(request):
    return render(request, 'new.html')


# 입력받은 내용을 DB에 넣는 함수
def create(request):
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/board/detail/' + str(board.id))

def newform(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BoardPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) # DB에 저장하지 않고 form에 임시 저장
            # 날짜는 자동으로 현재 입력해주는 것
            post.pub_date = timezone.now()
            post.save()
            return redirect('board')     # 바로 home으로 redirect
    
    # 2. 빈 페이지를 띄어주는 기능 -> GET
    else:
        form = BoardPost()
        return render(request, 'newform.html', {'form':form}) # form형태로 전달

# 삭제하기
def delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.delete()
    return redirect('board')

# 수정하기
def update(request,board_id):
    board=get_object_or_404(Board,pk=board_id)
    # 글을 수정사항을 입력하고 제출을 눌렀을 때
    if request.method == "POST":
        form = BoardPost(request.POST, request.FILES, instance=Board)
        if form.is_valid(): #error

                post=form.save(commit=False)
                
                # 검증에 성공한 값들은 사전타입으로 제공 
                print(form.cleaned_data)
                post.title = form.cleaned_data['title']
                post.body = form.cleaned_data['body']
                post.image = form.cleaned_data['image']
                post.pub_date = timezone.now()

                post.save()
                return redirect('/detail/'+board_id)

    # 수정사항을 입력하기 위해 페이지에 처음 접속했을 때
    else:
        form = BoardPost(instance = board)
        # 기존 내용 불러오기
        context={
            'form':form,
            'writing':True,
            'now':'update',
        }
        return render(request, 'update.html',{'form':form})
        