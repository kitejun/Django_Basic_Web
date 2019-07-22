from django import forms
from .models import Board

# 모델 기반이 아닌 임의의 입력 공간을 만들시 ModelForm 이 아닌 Form 사용
class BoardPost(forms.ModelForm):
    class Meta:        # Meta Class
        model = Board
        # Blog클래스에서 title과 body만 가져옴
        fields = ['title', 'body', 'image'] 