from django.core.management.base import BaseCommand
from django.db.models import Q
from faker import Faker
from users.models import User


class Command(BaseCommand):
    help = 'Generate fake users with unique email addresses and usernames'

    def handle(self, *args, **kwargs):
        fake = Faker()
        created_users = 0

        while created_users < 1000:
            username = fake.user_name()
            email = fake.email()

            # Kullanıcı adı ve e-posta adresi benzersiz mi kontrol et
            if not User.objects.filter(Q(username=username) | Q(email=email)).exists():
                User.objects.create(
                    username=username,
                    email=email,
                    password=fake.password(),
                )
                created_users += 1

        self.stdout.write(self.style.SUCCESS('Fake users generated successfully.'))
