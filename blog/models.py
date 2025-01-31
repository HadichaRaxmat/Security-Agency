from django.db import models


class UserContact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    message = models.TextField()

    def __str__(self):
        return self.name



