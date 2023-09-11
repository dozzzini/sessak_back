from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(upload_to="", null=True, blank=True)
    like_num = models.PositiveIntegerField(default=0)
    view_num = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

   
    category = models.ForeignKey(
        "categories.Category", 
        max_length=10, 
        on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"