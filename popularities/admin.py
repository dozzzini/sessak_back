from django.contrib import admin
from .models import Popularity

# Register your models here.
@admin.register(Popularity)
class UserAdmin(admin.ModelAdmin):
    list_display = ("__str__",)