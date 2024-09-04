from django.contrib.auth import get_user_model
from django.contrib.auth.middleware import get_user
from django.shortcuts import render
from django.views import View


# Create your views here.
User = get_user_model()

def signup(request):
    model = User


def login(request):
    pass

def detail(request):
    pass

