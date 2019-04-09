from django import forms
from .models import Post,Image

#ModelForm: 자동으로 model에 맞는 form 을 구조화 시켜준다.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

#이미지 올리기 위해
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        # fields = '__all__'
        fields = ['file',]
        widgets = {
            'file' : forms.FileInput(attrs={'multiple': True})
        }
        
        