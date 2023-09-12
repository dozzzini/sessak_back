from django.contrib import admin
from .models import Popularity


# Register your models here.
@admin.register(Popularity)
class UserAdmin(admin.ModelAdmin):
    list_display = ["post_list", "total_num"]
    list_display_links = ["post_list"]
