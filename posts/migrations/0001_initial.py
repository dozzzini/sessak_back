# Generated by Django 4.2.5 on 2023-10-06 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='게시글 제목')),
                ('content', models.TextField(verbose_name='게시글 내용')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='첨부파일')),
                ('view_num', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='게시글 작성날짜')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='게시글 수정날짜')),
            ],
        ),
    ]
