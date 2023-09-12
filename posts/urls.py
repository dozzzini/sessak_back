from django.urls import path
from . import views

urlpatterns = [
    path("newpost/", views.NewPost.as_view()),
]
