# Generated by Django 4.2.5 on 2023-09-14 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_post',
            field=models.ManyToManyField(blank=True, related_name='like_users', to='posts.post', verbose_name='좋아요 누른 사람'),
        ),
    ]
