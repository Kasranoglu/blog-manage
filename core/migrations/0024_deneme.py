# Generated by Django 4.2.4 on 2023-09-13 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deneme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
    ]
