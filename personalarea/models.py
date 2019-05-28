from django.db import models
from django.utils.translation import gettext as _

class New_personal(models.Model):
    """
    Модель нового сотрудника
    """
    login = models.CharField(_('Логин '), max_length=50, blank=True)
    password = models.CharField(_('Пароль '), max_length=50, blank=True)
    email = models.CharField(_('Электронная почта '), max_length=50, blank=True)
    first_name = models.CharField(_('Имя '), max_length=30, blank=True)
    last_name = models.CharField(_('Фамилия '), max_length=30, blank=True)
    phone = models.CharField(_('Телефон '), max_length=20, blank=True)

    class Meta:
        verbose_name = 'Новый персонал'
        verbose_name_plural = 'Новые персоналы'

class Personalarea(models.Model):
    """
    Модель личного кабинета
    """
    login = models.CharField(_('Логин '), max_length=50, blank=True)
    password = models.CharField(_('Пароль '), max_length=50, blank=True)
    email = models.CharField(_('Электронная почта '), max_length=50, blank=True)
    first_name = models.CharField(_('Имя '), max_length=30, blank=True)
    last_name = models.CharField(_('Фамилия '), max_length=30, blank=True)
    phone = models.CharField(_('Телефон '), max_length=20, blank=True)
    position = models.ManyToManyField(New_personal)

    class Meta:
        verbose_name = 'Личный кабинет'
        verbose_name_plural = 'Личные кабинеты'


