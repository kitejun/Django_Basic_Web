from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('', views.board, name='board'),
    path('newblog/', views.blogpost, name='newblog'),
    path('detail/<int:blog_id>', views.detail, name="detail"),
    path('detail/<int:blog_id>/delete', views.delete, name="delete"),
]