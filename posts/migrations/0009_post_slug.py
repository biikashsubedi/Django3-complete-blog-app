# Generated by Django 3.1.1 on 2020-09-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='slug', max_length=20, null=True),
        ),
    ]
