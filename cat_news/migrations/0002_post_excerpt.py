# Generated by Django 4.2.9 on 2024-01-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]
