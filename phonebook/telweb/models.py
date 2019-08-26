from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    patronymic = models.CharField(max_length=25)
    in_tel_num = models.CharField(max_length=5)


