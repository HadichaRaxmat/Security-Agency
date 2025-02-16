#!/bin/sh

echo "Waiting for PostgreSQL to start..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 1
done

echo "PostgreSQL started!"

# Запускаем миграции
python manage.py migrate

# Создаём суперпользователя, если его нет
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
email = "a@email.com"

if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(email=email, password="admin", username="admin")
    print("Superuser created")
else:
    print("Superuser already exists")
EOF

# Запускаем сервер
exec python manage.py runserver 0.0.0.0:8000
