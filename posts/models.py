from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Post(models.Model):
    #max_length 꼭 넣어줘야함.
    content = models.CharField(max_length=100)
    # image = models.ImageField(blank=True)
    #이미지 수정 기능 넣기위해 위의 코드 수정
    image = ProcessedImageField(
            upload_to='posts/images', #저장 위치
            processors=[ResizeToFill(600,600)], #크기지정
            format='JPEG',
            options={'quality':90},

    )
