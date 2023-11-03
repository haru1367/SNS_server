from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SNSSerializer
from .models import User_info
# Create your views here.

class SNS_View_Set(viewsets.ModelViewSet):
    queryset = User_info.objects.all()
    serializer_class = SNSSerializer
    
