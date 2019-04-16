from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

# Create your models here.

class Post(models.Model):
    #max_length 꼭 넣어줘야함.
    content = models.CharField(max_length=100)
    #user를 변수화 해서 넣는 형태
    #1:N관계 형성 , 사용자 한명이 자기가 쓴 게시물 여러개 가질 수 있다/
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # user를 변수화해서 넣음.
    
    # 좋아요 기능 추가
    # N:M 관계
    # 가운데 있는 모델을 자동으로 생성해준다. 무엇과 연결할지 알려줘야함.
    # 온딜리트 자동 설정 됨.
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_post_set", blank=True)

    #작성한 유저 저장 좋아요를 누른 유저 저장. 



#post image 1:N 관계로 묶어주기
class Image(models.Model):
    #CASCADE
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
     # image = models.ImageField(blank=True)
    #이미지 수정 기능 넣기위해 위의 코드 수정
    #원래 immage였지만 file로 바꿔서 사용
    file = ProcessedImageField(
            upload_to='posts/images', #저장 위치
            processors=[ResizeToFill(600,600)], #크기지정
            format='JPEG',
            options={'quality':90},

    )
# 코멘트는포스트 글에 속해 있음..
class Comment(models.Model):
    #외래키 필요
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # user한명이 comment 여러개 작성 가능
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length= 100)
    #작성한 시간 변수 autonow:게시물을 처음 생성할 때만 저장 created:수정
    created_at = models.DateTimeField(auto_now_add = True)
    
# # 좋아요 기능 추가
# class Like(models.Model):
#     post = models.ForeignKey(Post,on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)