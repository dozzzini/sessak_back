from django.urls import path
from . import views

urlpatterns = [
    path("newpost/", views.NewPost.as_view()),
    path("<int:pk>/", views.PostDetails.as_view()),
]
