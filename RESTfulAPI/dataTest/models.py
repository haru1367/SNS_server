from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.CharField(max_length=50) #이메일
    password = models.CharField(max_length=20) #비밀번호
    name = models.CharField(max_length=10) #이름
    address = models.TextField() #주소
    phone_number = models.CharField(max_length=15)#번호
    age = models.IntegerField() #나이
    dateTimeOfPosting = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['dateTimeOfPosting']

    