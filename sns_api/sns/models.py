from django.db import models

# Create your models here.

class User_info(models.Model):
    sns_email = models.CharField(max_length=50) # 아이디
    sns_password = models.CharField(max_length=15) #비밀번호
    
    def __str__(self):
        return self.sns_email