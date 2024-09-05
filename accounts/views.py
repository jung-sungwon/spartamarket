from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import get_user
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer


# Create your views here.

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # 유효성 검사 실패 시, 에러 응답 반환
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)



def login(request):
    pass

def detail(request):
    pass

