from django.shortcuts import render

# Restframework에서 불러온 것들
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response

# 모델 불러오기
from .models import Post

# serializers 불러오기
from .serializers import PostSerializer


# 새 게시글 작성 API
class NewPost(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_post = serializer.save()
        return Response(
            PostSerializer(new_post).data,
            status=status.HTTP_201_CREATED,
        )


# 게시글 조회, 수정 , 삭제 API
class PostDetails(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        print("해당 게시글:", post)
        serializer = PostSerializer(
            post,
            data=request.data,
            partial=True,
        )
        print("serializer_1: ", serializer)
        if serializer.is_valid():
            updated_post = serializer.save()
            return Response(
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
