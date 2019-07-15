from django import forms
from .models import CRUD_Blog

class CRUD_NewBlog(forms.ModelForm):
    class Meta:
        models = CRUD_Blog
        # fields = '__all__'     # 전부 입력 받고 싶을 때
        fields = ['title', 'body']