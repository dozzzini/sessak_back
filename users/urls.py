from django.urls import path
from . import views, social_login

urlpatterns = [
    path("userinfo/", views.UserInfo.as_view(), name="user-update"),
    path(
        "google/login/",
        social_login.google_login,
        name="google_login",
    ),
    path(
        "google/callback/",
        social_login.google_callback,
        name="google_callback",
    ),
    path(
        "google/login/finish/",
        social_login.GoogleLogin.as_view(),
        name="google_login_todjango",
    ),
]
