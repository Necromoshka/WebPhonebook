from django.db import models

# Create your models here.

class Organization(models.Model):
    filial=models.CharField(max_length=50, verbose_name='Филиал', db_index=True, unique=True)
    def __str__(self):
        return self.filial

    class Meta:
        verbose_name_plural='Филиалы'
        verbose_name = 'Филиал'
        ordering = ['filial']

class Cabinet(models.Model):
    room = models.CharField(max_length=4, verbose_name='Номер комнаты', db_index=True)
    org = models.ForeignKey('Organization', null=True, on_delete=models.PROTECT, verbose_name='Филиал', related_name='entries', related_query_name='entry')
    def __str__(self):
        return self.room

    class Meta:
        verbose_name_plural='Кабинеты'
        verbose_name = 'Кабинет'
        ordering = ['room']


class InTel(models.Model):
    tel = models.CharField(max_length=4, verbose_name='Внутренний номер', db_index=True, unique=True)
    in_room = models.ForeignKey('Cabinet', null=True, on_delete=models.PROTECT, verbose_name='Номер кабинета', related_name='entries', related_query_name='entry')
    def __str__(self):
        return self.tel

    class Meta:
        verbose_name_plural='Телефоны'
        verbose_name = 'Телефон'
        ordering = ['tel']

class Person(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя')
    surnsurnameame = models.CharField(max_length=25, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=25,verbose_name='Отчество')
    mob_tel_num = models.CharField(max_length=15, null=True, blank=True, verbose_name='Мобильный телефон')
    em = models.EmailField(null=True,blank=True,verbose_name='Email')
    subdivision = models.CharField(max_length=25, db_index=True,verbose_name='Номер подраздиления')
    extension = models.ForeignKey('InTel', null=True, on_delete=models.PROTECT, verbose_name='Внутренний номер', related_name='entries', related_query_name='entry')


    class Meta:
        verbose_name_plural='Абоненты'
        verbose_name = 'Абонент'
        ordering = ['subdivision']





# class In_tel(models.Model):
