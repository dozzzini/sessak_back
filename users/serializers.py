from rest_framework import serializers
from .models import User  # 사용자 모델을 import


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "nickname",
        ]
