from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Board
from django.core.paginator import Paginator
# form.py에서 가져옴
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
    # request된 페이지를 얻어온 뒤 return 해 준다.
    posts = paginator.get_page(page)
    
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
        form = BoardPost(request.POST)
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