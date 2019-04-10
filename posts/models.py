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
    