from django.urls import path
from . import views
app_name = "accounts"

urlpatterns = [
    #signup으로 들어오면 회원가입 폼 볼수있게 , 회원가입 시켜주기 작업이 필요함.
    path('signup/', views.signup, name='signup'),
    ]