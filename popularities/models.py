from django.db import models


# Create your models here.
class Popularity(models.Model):
    name = models.CharField(
        default="인기글",
        max_length=10,
    )
    post_list = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        verbose_name="인기 게시글",
    )
    total_num = models.PositiveIntegerField(
        verbose_name="총합",
    )

    def __str__(self) -> str:
        return f"{self.post_list}"

    # total_num에 대한 합산 처리
