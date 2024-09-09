from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import get_user
from django.shortcuts import render
from django.template.context_processors import request
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer, UserCreateSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class SignupView(APIView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            self.permission_classes = [AllowAny]
        elif request.method == "DELETE":
            self.permission_classes = [IsAuthenticated]
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user.delete()
        logout(request)
        return Response(
            {"message": "다음에 다시 만나요"}, status=status.HTTP_204_NO_CONTENT
        )


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": "username 또는 password 가 틀렸습니다."},
            status=status.HTTP_400_BAD_REQUEST,
        )


class Userprofile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserCreateSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
