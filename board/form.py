from django import forms
from .models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        # Blog클래스에서 title과 body만 가져옴
        fields = ['title', 'body'] 

