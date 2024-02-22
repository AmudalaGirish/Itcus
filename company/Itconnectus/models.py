from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


