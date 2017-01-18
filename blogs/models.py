from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Article(models.Model):
    title = models.CharField('title', max_length=256)
    content = models.TextField('content')
    author = models.CharField('author',max_length=256)

    pub_date = models.DateTimeField('published date',auto_now_add=True)
    edit_date=models.DateTimeField('edited date', auto_now=True)

    def __str__(self):
    	return self.title



# class User(models.Model):
# 	username=models.CharField('username',max_length=256)
# 	nickname=models.CharField('nickname',max_length=256)
# 	email=models.EmailField('email')
# 	phone=models.IntegerField('phone')
# 	address=models.CharField('address',max_length=256)




