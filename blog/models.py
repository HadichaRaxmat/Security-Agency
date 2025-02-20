from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if 'role' not in extra_fields:
            extra_fields['role'] = 'superuser'

        if not username:
            raise ValueError("Superuser must have a username.")

        return self.create_user(email, password, username, **extra_fields)


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('superuser', 'Superuser'),
        ('admin_manager', 'Admin Manager'),
        ('moderator', 'Moderator'),
        ('editor', 'Editor'),
        ('support', 'Support'),
        ('admin', 'Admin'),
    ]

    avatar = models.ImageField(upload_to='avatar_photos/', null=True, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='admin')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.is_superuser and not self.is_staff:
            raise ValidationError("Superuser must have is_staff=True.")
        if not self.is_active and self.is_superuser:
            raise ValidationError("Superuser cannot be deactivated.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} ({self.role})"


class UserContact(models.Model):
    STATUS_CHOICES = [
        ('unread', 'Unread'),
        ('read', 'Read'),
    ]

    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unread')

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"





class Header(models.Model):
    logo = models.CharField(max_length=100)

    def __str__(self):
        return self.logo


class Menu(models.Model):
    MENU_CHOICES = [
        ("HOME", "HOME"),
        ("SERVICES", "SERVICES"),
        ("GUARDS", "GUARDS"),
        ("CONTACT US", "CONTACT US"),
        ("ABOUT", "ABOUT"),
    ]

    menu = models.CharField(max_length=100, choices=MENU_CHOICES, unique=True)
    title = models.CharField(max_length=100, default="")
    is_active = models.BooleanField(default=True)

    def get_url(self):
        menu_urls = {
            "HOME": "/",
            "SERVICES": "/service/",
            "GUARDS": "/guard/",
            "CONTACT US": "/contact/",
            "ABOUT": "/about/",
        }
        return menu_urls.get(self.menu, "#")

    def __str__(self):
        return self.title or dict(self.MENU_CHOICES).get(self.menu, "Unknown")




class HeaderTouch(models.Model):
    method = models.CharField(max_length=50)

    def __str__(self):
        return self.method


class Slider(models.Model):
    image = models.ImageField(upload_to='banner_photos/', blank=True, null=True)
    title = models.CharField(max_length=100)
    title_continue = models.CharField(max_length=100)
    text = models.CharField(max_length=350)
    last = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class About(models.Model):
    image = models.ImageField(upload_to='slider_photos/', blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    last = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class ServiceHeader(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Service(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300)
    last = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Client(models.Model):
    image = models.ImageField(upload_to='client_photos/', blank=True, null=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Touch(models.Model):
    image = models.ImageField(upload_to='touch_photos/', blank=True, null=True)
    title = models.CharField(max_length=50)
    last = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Team(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=400)
    last = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class Guard(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    image = models.ImageField(upload_to='guard_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Info(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)

    def __str__(self):
        return  self.title



class ContactUs(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title




class Subscribe(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    last = models.CharField(max_length=100)

    def __str__(self):
        return self.title




class Footer(models.Model):
    info = models.CharField(max_length=100)

    def __str__(self):
        return self.info