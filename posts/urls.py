# url경로를 더 직관적으로 사용하기 위해 name을 사용하려면 app_name 설치

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.list, name='list'),    
]