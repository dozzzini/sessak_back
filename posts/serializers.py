from rest_framework.serializers import ModelSerializer
from .models import Post
from rest_framework import serializers
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer
from comments.serializers import CommentSerializer


class PostSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    post_comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = "__all__"
