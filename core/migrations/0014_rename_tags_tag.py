# Generated by Django 4.2.4 on 2023-09-12 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_post_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]