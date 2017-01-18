from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ShortURL(models.Model):
    url=models.CharField(max_length=220,unique=True)
    shortcode=models.CharField(max_length=15,unique=True,blank=True)
    updated=models.DateTimeField(auto_now=True) #everytime the model is saved
    timestamp=models.DateTimeField(auto_now_add=True) #when model was created
    active=models.BooleanField(default=True)