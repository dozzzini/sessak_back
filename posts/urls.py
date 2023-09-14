from django.urls import path
from . import views

urlpatterns = [
    path("newpost/", views.NewPost.as_view()),
    path("<int:pk>/", views.PostDetails.as_view()),
    path("like/<int:post_id>", views.like_post, name="like_post"),
]
