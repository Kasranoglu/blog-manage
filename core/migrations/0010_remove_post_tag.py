# Generated by Django 4.2.4 on 2023-09-12 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
    ]
