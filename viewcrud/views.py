from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'funccrud.html', {'blogs', blogs})