# Generated by Django 4.2.5 on 2023-09-25 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='게시글 작성자'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(max_length=10, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.category', verbose_name='카테고리'),
        ),
        migrations.AddField(
            model_name='post',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_posts', to=settings.AUTH_USER_MODEL, verbose_name='좋아요 누른 사람'),
        ),
    ]
