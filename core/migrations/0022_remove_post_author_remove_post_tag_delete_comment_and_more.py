# Generated by Django 4.2.4 on 2023-09-13 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
