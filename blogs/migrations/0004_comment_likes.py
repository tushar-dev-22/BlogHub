# Generated by Django 5.0.7 on 2024-07-31 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog_likes_comment'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to='users.customuser'),
        ),
    ]
