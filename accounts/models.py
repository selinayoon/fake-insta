from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings 

# Create your models here.
class User(AbstractUser):
    # m:n 으로 연결
    # blank 팔로우 아무도 안해도 돼
    # follow = models.ManyToManyField(어떤 모델과 연결,related_name="",blank=True)
    # 방법 1
    #follow = models.ManyToManyField(self,related_name="",blank=True)
    
    #방법 2
    #Auth_User_model 사용할 때 설치했던 모듈(from django.conf import settings ) 설치
    # follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="follower",blank=True)
    
    # 네이밍 수정하기
    # 팔로우 하는사람들의 목록
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers",blank=True)
    introduce = models.TextField()
    #자기소개란 
    
    #이미지 업뎃
    profile_image = ProcessedImageField(
            upload_to='accounts/images', # 저장 위치
            processors=[ResizeToFill(150,150)], # 크기 지정
            format='JPEG',
            options={'quality':90}, # 원본의 90% 품질로 저장
            blank=True
        )
    
    
    
    def __str__(self):
        return self.username
        
    