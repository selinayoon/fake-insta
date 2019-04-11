from django import forms
from .models import Post,Image,Comment

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
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__' # 입력을 받을 수 있도록 사용자에게 보여주는 곳  
        fields = ['content',] # content만 입력받으면 되기 때문에!!!!!!!!!! #, 는 안적어도 되나 실수 방지용
        