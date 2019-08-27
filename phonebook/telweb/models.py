from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя')
    surnsurnameame = models.CharField(max_length=25, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=25,verbose_name='Отчество')
    mob_tel_num = models.CharField(max_length=11, null=True, blank=True, verbose_name='Мобильный телефон')
    em = models.EmailField(null=True,blank=True,verbose_name='Email')
    subdivision = models.CharField(max_length=25, db_index=True,verbose_name='Номер подраздиления')


    class Meta:
        verbose_name_plural='Абоненты'
        verbose_name = 'Абонент'
        ordering = ['subdivision']

# class In_tel(models.Model):
