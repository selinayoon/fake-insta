from django import forms
from .models import Post,Image

#ModelForm: 자동으로 model에 맞는 form 을 구조화 시켜준다.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # # content와 user의 정보를 다 보여줘
        # fields = '__all__'
        #컨텐츠만 보여줘
        fields = ['content',]

#이미지 올리기 위해
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        # fields = '__all__'
        fields = ['file',]
        widgets = {
            'file' : forms.FileInput(attrs={'multiple': True})
        }
        
        