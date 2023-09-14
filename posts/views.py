from django.shortcuts import render
from rest_framework.decorators import api_view

# Restframework에서 불러온 것들
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

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
        print("ㄱㄴㄱㄴ", post)
        print("안 바뀐 거", post.view_num)
        post.view_num = post.view_num + 1
        print("바뀐 거", post.view_num)
        post.save()
        print("바뀐 post", post)
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


# 좋아요 추가 및 취소
@api_view(["POST"])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    print(dir(request.user))
    if post.like_users.filter(pk=request.user.pk).exists():
        # 넌 취소를 할 수 있어
        post.like_users.remove(request.user.pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        # 만약 안 들어와있어
        post.like_users.add(request.user.pk)
        # 그럼 누를 수 있어
        return Response(status=status.HTTP_200_OK)


# 게시물 검색 - 제목 또는 내용
class SearchPost(APIView):
    def post(self, request):
        pass


# 조회수
# @api_view(["GET"])
# def view_post(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#         post.view_num += 1
#         post.save()
#         serializer = PostSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     except ObjectDoesNotExist:
#         return Response({"message": "게시글을 찾을 수 없습니다"}, status=status.HTTP_404_NOT_FOUND)
