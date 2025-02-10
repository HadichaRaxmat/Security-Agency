from django.core.management.base import BaseCommand
from blog.models import CustomUser

class Command(BaseCommand):
    help = 'Creates a custom superuser'

    def handle(self, *args, **kwargs):
        email = input("Enter email: ")
        password = input("Enter password: ")
        username = input("Enter username: ")

        # Создаем суперпользователя с правильной ролью
        user = CustomUser.objects.create_superuser(
            email=email,
            password=password,
            username=username,
            is_admin=True,  # Это можно убрать, так как superuser всегда admin
            role='superuser'  # <-- Добавлено
        )
        self.stdout.write(self.style.SUCCESS(f"Successfully created superuser: {user.email}"))

