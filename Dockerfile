# Используем официальный Python-образ
FROM python:3.10

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаём и переходим в рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app/

# Устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Устанавливаем PostgreSQL-клиент и netcat-openbsd
RUN apt-get update && apt-get install -y postgresql-client netcat-openbsd

# Копируем entrypoint-скрипт
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Используем entrypoint.sh для запуска контейнера
ENTRYPOINT ["/entrypoint.sh"]


