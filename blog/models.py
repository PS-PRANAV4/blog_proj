from django.db import models
from account.models import Accounts
# Create your models here.

class Post(models.Model):
    description = models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to = 'media/post',blank = True,null = True)
    likes = models.IntegerField(null=True,blank=True,default = 0)
    liked_persons = models.ManyToManyField(Accounts, null=True,blank=True)



class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(Accounts,on_delete=models.CASCADE,related_name='user')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post')