


#   python manage.py shell


#    python manage.py makemigrations
#    python manage.py migrate
#    python manage.py createsuperuser



from blog.models import CustomUser

# Создайте суперпользователя вручную
user = CustomUser.objects.create_superuser(
    email="admin@example.com",
    password="yourpassword",
    username="admin"
)

print(user)

# py manage.py create_custom_superuser


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}