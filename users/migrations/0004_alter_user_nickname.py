# Generated by Django 4.2.5 on 2023-10-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='IZllHAzCtA', max_length=10),
        ),
    ]