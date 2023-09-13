from django.shortcuts import render

# Restframework에서 불러온 것들
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import ValidationError, NotFound, PermissionDenied
from rest_framework.response import Response

# 모델 불러오기
from .models import Category
from posts.models import Post

# serializers 불러오기
from .serializers import CategorySerializer


# 새 키테고리 추가 API
class NewCategory(APIView):
    # permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_category = serializer.save()
            return Response(
                CategorySerializer(new_category).data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class CategoryDetails(APIView):
    # permission_classes=[IsAuthenticated]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
