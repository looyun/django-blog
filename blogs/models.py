from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
import os
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField('phone',blank=True)
    avatar = models.ImageField('avatar',upload_to='',default='/user.png')


class Article(models.Model):
    title = models.CharField('title', max_length=256)
    content = models.TextField('content')
    author = models.ForeignKey(User)

    views =models.IntegerField('views',default=0)
    reply_count =models.IntegerField('reply count',default=0)
    pub_date = models.DateTimeField('published date',auto_now_add=True)
    edit_date=models.DateTimeField('edited date')

    def __str__(self):
    	return self.title


class Comment(models.Model):
    article = models.ForeignKey('Article', verbose_name='Article', on_delete=models.CASCADE, default="")
    content = models.TextField('content')
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField('published date',auto_now_add=True)



# class User(models.Model):
# 	username=models.CharField('username',max_length=256)
# 	nickname=models.CharField('nickname',max_length=256)
# 	email=models.EmailField('email')
# 	phone=models.IntegerField('phone')
# 	address=models.CharField('address',max_length=256)




