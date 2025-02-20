[![Platform](https://img.shields.io/badge/platform-Windows-blue)](https://shields.io)
![Django](https://img.shields.io/badge/Django-5.1-green)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)

**Security Agency** – это кастомизированная система администрирования, построенная на Django и работающая в контейнерах Docker.

---

## 🚀 Установка и запуск

### 📌 Требования

Перед началом убедитесь, что у вас установлены:

- **Windows 10/11**
- **Python 3.10** (или выше)
- **PostgreSQL** (если используете базу данных локально)
- **Docker и Docker Compose** (если хотите запускать через контейнеры)
- **Git** (для клонирования репозитория)

Проверить установку можно командами:

```sh
docker --version
docker-compose --version
python --version
```

---

### 🔹 Клонирование репозитория

Сначала склонируйте проект с GitHub:

```sh
git clone https://github.com/HadichaRaxmat/Security-Agency.git
cd Security-Agency
```

---

### 🔹 Установка зависимостей (без Docker)

⚠️ **Важно:** По умолчанию проект настроен на использование базы данных в контейнере Docker. Если вы хотите запустить проект вручную без Docker, вам нужно изменить настройки базы данных в `settings.py` на вашу локальную базу данных, например PostgreSQL, MySQL или стандартную SQLite3. Например:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Или другой движок
        'NAME': 'your_local_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',  # Или IP-адрес сервера базы данных
        'PORT': '5432',  # Порт вашей базы данных
    }
}
```

После внесения изменений установите зависимости и выполните миграции:

```sh
python -m venv venv
source venv/Scripts/activate  # Для Windows
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
py manage.py create_custom_superuser  # (Введите данные для суперпользователя)
python manage.py runserver
```

Проект будет доступен по адресу:  
📍 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🔹 Запуск через Docker

#### **1️⃣ Сборка и запуск контейнеров**

```sh
docker-compose up --build
```

При первом запуске автоматически создаётся суперпользователь:

- **Email:** `a@email.com`
- **Логин:** `admin`
- **Пароль:** `admin`

После успешного запуска проект будет доступен по адресу:  
📍 [http://guarder:8000](http://guarder:8000)

#### **2️⃣ Остановка контейнеров**

```sh
docker-compose down
```

#### **3️⃣ Очистка неиспользуемых данных**

```sh
docker system prune -a  # Удаляет неиспользуемые контейнеры, образы и кэшированные слои
```

#### **4️⃣ Перезапуск контейнеров**

```sh
docker-compose up -d  # Запускает контейнеры в фоновом режиме (detached mode)
```

#### **5️⃣ Удаление контейнеров и всех данных (включая базу данных!)**

```sh
docker-compose down -v  # Останавливает контейнеры и удаляет все тома (включая БД)
```

#### **6️⃣ Перезапуск контейнеров без удаления данных**

```sh
docker-compose restart
```

---

## 🔗 Доступ к административной панели

После успешного запуска, админ-панель будет доступна по адресу:

📍 [http://guarder:8000/admin/](http://guarder:8000/admin/)

---

## 🛠 Дополнительная информация

- **Документация Django:** [Django Official Docs](https://docs.djangoproject.com/en/5.1/)
- **Документация Docker:** [Docker Docs](https://docs.docker.com/)

---

