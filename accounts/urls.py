from django.urls import path
from accounts import views


app_name = 'accounts'
urlpatterns = [
    path('', views.SignupView.as_view(), name='signup'),
    # path('login', views.LoginView.as_view(), nama="login"),
    path('<str:username>/', views.detail),
]