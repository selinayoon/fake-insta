# url경로를 더 직관적으로 사용하기 위해 name을 사용하려면 app_name 설치

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # id지정 하면 해당 id에만 작용, id지정 안하면 전체에 적용
    path('', views.list, name='list'),
    path('create/', views.create, name="create"),
    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),
    # 게시물의 아이디를 통해 어떤 게시물에 댓글을 달건지 지정
    path('<int:post_id>/comment/create/', views.comment_create, name="comment_create"), #id: postid
    path('<int:post_id>/comment/<int:comment_id>/delete/', views.comment_delete, name="comment_delete"),
    
    path('<int:id>/like/',views.like, name="like"),
]