from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.signinup),
    path('login/', views.login),
    path('<str:username>/', views.detail),

]