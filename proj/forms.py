from django import forms
from proj.models import Post_Normal, Photo

class Post_Normal_Form(forms.ModelForm):
    class Meta:
        model = Post_Normal
        fields = {'subject', 'content', 'image'}
        labels = {
            'subject': '제목',
            'content': '내용',
            'image': '이미지',
        }

class Photo_Form(forms.ModelForm):
    class Meta:
        model = Photo
        fields = {'images'}
        labels = {
            'images': '추가 이미지',
        }