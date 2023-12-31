# Generated by Django 4.2.4 on 2023-09-13 02:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0022_remove_post_author_remove_post_tag_delete_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('category', models.CharField(choices=[('nature-lifestyle', 'Nature Lifestyle'), ('awesome-layouts', 'Awesome Layouts'), ('creative-ideas', 'Creative Ideas'), ('responsive-templates', 'Responsive Templates'), ('creative-unique', 'Creative & Unique')], default='nature-lifestyle', max_length=100)),
                ('content', models.TextField(max_length=100000)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=100)),
                ('image', models.ImageField(default='blog-thumb-03_kQncFpU.jpg', upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(blank=True, to='core.tag')),
            ],
            options={
                'ordering': ('-updated_ad',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_comment', to='core.post')),
            ],
            options={
                'ordering': ('-updated_ad',),
            },
        ),
    ]
