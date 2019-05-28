from django.db import models
from django.utils.translation import gettext as _

class Confirmation(models.Model):
    """
    Модель подтверждения
    """
    email = models.EmailField(_('Электронная почта '), max_length=50, blank=True, unique=True)
    viber = models.CharField(_('Вайбер '), max_length=50, blank=True, unique=True)
    sms = models.CharField(_('СМС '), max_length=50, blank=True)

    class Meta:
        verbose_name = 'Подтверждение'
        verbose_name_plural = 'Подтверждения'
