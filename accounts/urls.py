from django.urls import path
from accounts import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

app_name = "accounts"

urlpatterns = [
    path("", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
    path("<str:username>/", views.Userprofile.as_view(), name="userprofile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
