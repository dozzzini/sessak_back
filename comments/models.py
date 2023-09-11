from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    comment_num = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="post_comments", null=True)


    def __str__(self) -> str:
        return f"{self.author} - {self.comment} / {self.post}"
