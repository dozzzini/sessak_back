from django.shortcuts import render

from rest_framework.views import APIView
from .models import Post

# Create your views here.


# 새 게시글 작성 API
class NewPost(APIView):
    def post(self, request):
        pass
