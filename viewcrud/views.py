from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import CRUD_Blog
from .form import CRUD_NewBlog

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    crud_blogs = CRUD_Blog.object.all()
    return render(request, 'viewcrud/funccrud.html', {'crud_blogs', crud_blogs})

def create(request):
    return 

def update(request):
    return

def delete(request):
    return
