# Generated by Django 4.2.4 on 2023-09-12 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_tags_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='isim',
            new_name='name',
        ),
    ]