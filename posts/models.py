from django.db import models

# Create your models here.

class Post(models.Model):
    #max_length 꼭 넣어줘야함.
    content = models.CharField(max_length=100)

