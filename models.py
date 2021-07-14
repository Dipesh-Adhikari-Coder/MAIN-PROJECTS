from django.db import models
from django.urls import reverse


# Create your models here.
class AdminUsers(models.Model):
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return reverse("AdminUsers", kwargs={"email": self.email})


class RegisteredUsers(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return reverse("RegisteredUsers", kwargs={"name": self.name})
