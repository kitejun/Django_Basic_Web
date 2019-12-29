# Django 학습 프로젝트
##  Django의 기본 기능들이 모두 들어간 Web구현

__김연준(단독)__

### 0. 개요
------------------------------
1. Web framework 중 하나인 Django를 학습하여 Django마스터가 되고자 한다.
<p align="center"><img src="http://taking.kr/blog/wp-content/uploads/2014/08/laravel.png"></p>

### 1. 제작 목적
------------------------------
기본기능을 통한 실력 향상

### 2. 역할 분담
------------------------------
 * 김연준: 백엔드, 프론트엔드, DB

### 3. 참고
------------------------------
 * https://www.djangoproject.com/                 -> 공식 한국 페이지
 * https://www.djangoproject.com/                 -> 공식 페이지
 
### 4. Detail
------------------------------
* Framework: Django
 * Tool: Visual Code
 * 언어: python
 * DB: SQLite
 
 ### 5. 학습노트
------------------------------
<<Django>>
장고는 ORM(Object Relational Mapping) 방식으로 DB를 다룸
: 정의하고자 하는 데이터를 클래스(객체)로 표현 객체로 (관계형) DB를 다룬다.(models.py 에서 데이터 정의 후 python manage.py makemigrations로 DB에 저장
장고는 데이터를 추가 열람 수정 삭제 (CRUD) 방식으로 데이터를 다룸 -> 함수&클래스로 구현

===================================
1. python -m venv myvenv(가상환경명) : 가상환경 생성
2. source myvenv/Scripts/activate : 가상환경 실행(일종의 메모리이다. 따라서 가상환경이 실행되어 있지 않으면 저장되어있는 프레임워크인 django도 실행 못함)
+ deactivate : 가상환경 끄기
+ pip install django : 장고 설치(초기 가상환경에 장고가 없을때만 설치)
3. django-admin startproject projectname : 새 프로젝트 생성(모든 작업에 프로젝트는 오직 1개)
4. python manage.py startapp 앱이름 : 프로젝트에 앱 추가(앱이란 프로젝트의 기능을 추가할떄마다 생성하는 것) 
->블로그로 예를 들면 (게시판),  (로그인,회원가입), (워드카운트 기능) 이렇게 하나의 기능을 만들떄
앱 추가
5. settings.py 에 " 'App이름.apps.App이름Config' " 추가 : App이 생성 되면 프로젝트에 App이 생성되었다는 것을 알려줘야한다.
6. App에 templates폴더 생성 후 .html 파일 생성
7. views.py에 .html 파일의 위치를 알려주는 함수 or 기능을 수행하는 함수 추가(ex)로그인 기능, 회원가입기능)
8. urls.py 에 url 경로 설정: url에 따라 views.py에 선언된 함수를 불러오고 .html파일 실행
9.  python manage.py runserver: 서버켜기( ★중요: 작업한 .html & .py 파일을 Ctrl+s 로 각각 다 저장해야한다.)
10. python manage.py makemigrations
      python manage.py migrate               : DB migrate하기
===============================================================
관리자(admin)을 만들 경우
1. python manage.py createsuperuser  : 관리자(admin) 계정 만들기(아이디, 비번 설정해준다 생각하면 된다.)
2. models.py 에 클래스를 만든다.: /admin 에서 추가 할 수 있는 형식을 지정 해준다(ex) 제목, 날짜, 내용 글, 사진....)
3. admin.py에 models.py에 추가한 클래스를 등록(regiter)해준다. : 즉 등록을 안 해주면 models.py에 admin 글쓰는 형식을 정해줘도 /admin 에 나타나지 않는다. 꼭! models.py 에 형식 지정 후 등록해줘야한다.( ex) dmin.site.register(Blog) )
4. python manage.py collectstatic
===============================================================
★ 자주 발생되는 일들 ★
1. .py & .html 을 만들어주고 저장을 안 한다. : 각각 파일마다 Ctrl + s 를 해주던가 오른쪽 마우스 클릭 후 모두 닫기를 누르면 저장하지 못했던 파일들을 알려주고 "저장" 클릭
2. 들여쓰기 문제: 파이썬은 중괄호{} 로 코드를 구별하지 않고 들여쓰기로 구별한다. 함수 나 클래스를 생성 후 들여쓰기가 잘 되어있는지 확인하자
3. 가상환경을 실행하지 않고 서버를 돌린다. : 가상환경을 실행하지 않으면 그 안 에 프레임워크인 django도 실행되지 않는다. 가상환경인 (myvenv) 가 실행되어있는지 확인하자
