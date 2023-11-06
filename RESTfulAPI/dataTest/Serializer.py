from rest_framework import serializers
from .models import Users

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','email','password','name','address','phone_number','age']