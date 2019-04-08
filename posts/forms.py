from django import forms
from .models import Post

#ModelForm: 자동으로 model에 맞는 form 을 구조화 시켜준다.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'