from rest_framework import serializers
from .models import User_info

class SNSSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = ('id','sns_email','sns_password')