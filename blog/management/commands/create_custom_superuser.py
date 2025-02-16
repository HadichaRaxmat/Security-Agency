from django.core.management.base import BaseCommand
from blog.models import CustomUser

class Command(BaseCommand):
    help = "Creates a custom superuser"

    def handle(self, *args, **kwargs):
        email = "a@email.com"
        password = "admin"
        username = "admin"

        if not CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.create_superuser(
                email=email,
                password=password,
                username=username,
                role="superuser"
            )
            self.stdout.write(self.style.SUCCESS(f"Successfully created superuser: {user.email}"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists."))


