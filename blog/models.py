from django.db import models


class UserContact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    message = models.TextField()

    def __str__(self):
        return self.name



class Header(models.Model):
    logo = models.CharField(max_length=20)

    def __str__(self):
        return self.logo


class Menu(models.Model):
    menu = models.CharField(max_length=20)

    def __str__(self):
        return self.menu



class HeaderTouch(models.Model):
    method = models.CharField(max_length=50)

    def __str__(self):
        return self.method


class Slider(models.Model):
    image = models.ImageField(upload_to='blog/banner_photos/', blank=True, null=True)
    title = models.CharField(max_length=100)
    title_continue = models.CharField(max_length=100)
    text = models.CharField(max_length=350)
    last = models.CharField(max_length=100)

    def __str__(self):
        return self.title



class About(models.Model):
    image = models.ImageField(upload_to='blog/slider_photos/', blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=400)
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
    image = models.ImageField(upload_to='blog/client_photos/', blank=True, null=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Touch(models.Model):
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
    image = models.ImageField(upload_to='blog/guard_photos/', blank=True, null=True)

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