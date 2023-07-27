from django.db import models
from django.contrib.auth.models import User

class candidate(models.Model):	
    user = models.ForeignKey(User,null = True,on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add =True,null = True)
    


class worker(models.Model):	
    user = models.ForeignKey(User,null = True,on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=200)
    designation = models.CharField(max_length=200,null = True)
    created_at = models.DateTimeField(auto_now_add =True,null = True)


class search(models.Model):	
    userid = models.IntegerField(default=0)
    message = models.CharField(max_length=1000)
