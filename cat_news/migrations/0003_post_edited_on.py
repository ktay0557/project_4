# Generated by Django 4.2.9 on 2024-01-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_news', '0002_post_excerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='edited_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]