import random
from faker import Faker
from django.contrib.auth.models import User
from users.models import Post, Tag, Like
from users.constants import CATEGORY_CHOICES, STATUS_CHOICES, CREATIVE_UNIQUE, DEFAULT_BLOG_IMAGE, STATUS_DRAFT, \
    CONFIRMATION_CHOICES, CONFIRMATION_WAIT
from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    help = 'Generate 1000 fake posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()  # Mevcut kullanıcıları alın

        for _ in range(1000):
            post = Post(
                title=fake.sentence(),
                subtitle=fake.sentence(),
                author=random.choice(users),
                category=random.choice(CATEGORY_CHOICES)[0],
                content=fake.paragraph(nb_sentences=10),
                status=random.choice(STATUS_CHOICES)[0],
                image=DEFAULT_BLOG_IMAGE,
                confirmation=random.choice(CONFIRMATION_CHOICES)[0],
            )
            post.save()  # Post'u kaydet

            # Rastgele etiketler oluşturun ve ekleyin
            num_tags = random.randint(1, 5)
            for _ in range(num_tags):
                tag = Tag(name=fake.word())
                tag.save()
                post.tag.add(tag)



        self.stdout.write(self.style.SUCCESS('1000 fake posts generated successfully.'))
