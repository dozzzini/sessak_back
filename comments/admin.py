from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    list_display = ("__str__",)