from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Users
from .Serializer import userSerializer

@csrf_exempt
def user_list(request):
    if request.method == 'GET': # GET 방식일 때
        query_set = Users.objects.all() # ORM으로 Users의 모든 객체 받아옴
        serializer = userSerializer(query_set, many=True) # JSON으로 변환
        return JsonResponse(serializer.data, safe=False) # JSON타입의 데이터로 응답

    elif request.method == 'POST': # POST방식일 때
        data = JSONParser().parse(request) # 요청들어온 데이터를 JSON 타입으로 파싱
        serializer = userSerializer(data=data) # Serializer를 사용해 전송받은 데이터를 변환하기 위함
        if serializer.is_valid(): # 생성한 모델과 일치하면
            serializer.save() # 데이터 저장
            return JsonResponse(serializer.data, status=201) # 정상 응답 201
        return JsonResponse(serializer.errors, status=400) # 모델에 일치하지 않는 데이터일 경우

@csrf_exempt
def user_select(request,pk):
    object = Users.objects.get(pk=pk)
    if request.method == "GET":
        serializer = userSerializer(object)
        return JsonResponse(serializer.data,safe = False)
    
    elif request.method == "PUT":
        update_data = JSONParser().parse(request)
        serializer = userSerializer(object,data=update_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)
    
    elif request.method == "DELETE":
        object.delete()
        return HttpResponse(status=204)
        