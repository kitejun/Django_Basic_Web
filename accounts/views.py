from django.shortcuts import render, redirect
# login 과정 import
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':  # POST 방식으로 form을 설정해주었기 때문에
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            # 계정 생성
            auth.login(request, user)  # 회원가입하면 자동 로그인 될 수 있게
            return redirect('home')  # 로그인되면 home으로
    return render(request, 'signup.html')  # 회원가입이 실패하면 회원가입 페이지에 머물기


def login(request):
    if request.method == 'POST':  # POST 방식으로 form을 설정해주었기 때문에
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # DB에서 회원정보가 있는지 저장되어있는지 확인하는 함수
        if user is not None:  # 이미 존재하는 회원이라면
            auth.login(request, user)
            return redirect('home')
        else:  # 회원이 아니라면
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')