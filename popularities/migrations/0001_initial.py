# Generated by Django 4.2.5 on 2023-09-12 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Popularity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='인기글', max_length=10)),
                ('total_num', models.PositiveIntegerField(verbose_name='총합')),
            ],
        ),
    ]
