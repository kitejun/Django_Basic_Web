from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name='board'),
    # 그냥 생성
    path('new', views.new, name='new'),
    # form 형식으로 생성
    path('newform/',views.newform,name="newform"),

    path('create/', views.create, name='create'),
    path('detail/<int:board_id>', views.detail, name="detail"),

    path('detail/<int:board_id>/delete', views.delete, name="delete"),
]