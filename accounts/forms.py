from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username','email',]
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        # fields = '__all__'
        # 필요한 정보만 가져오기
        fields = ['email','introduce','profile_image',]