from django.db import models
from django.utils.translation import gettext as _


class Company(models.Model):
    """
    Модель компании
    """
    name = models.CharField(_('Название '), max_length=50, blank=True)
    inn = models.CharField(_('ИНН '), max_length=20, blank=True)
    ogrn = models.CharField(_('ОГРН '), max_length=50, blank=True)
    kpp = models.CharField(_('КПП '), max_length=50, blank=True)
    address = models.CharField(_('Адрес '), max_length=300, blank=True)
    post_address = models.CharField(_('Юридический адрес '), max_length=300, blank=True)
    phone = models.CharField(_('Телефон '), max_length=20, blank=True)
    name_director = models.CharField(_('Имя директора '), max_length=50, blank=True)
    last_name_director = models.CharField(_('Фамилия директора '), max_length=50, blank=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Position(models.Model):
    """
    Модель должности персонала
    """
    position = models.CharField(_('Должность '), max_length=200, help_text="Должность человека", blank=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Personal(models.Model):
    """
    Модель персонала
    """
    first_name = models.CharField(_('Имя '), max_length=30, blank=True)
    last_name = models.CharField(_('Фамилия '), max_length=30, blank=True)
    phone = models.CharField(_('Телефон '), max_length=20, blank=True)
    email = models.EmailField(_('Электронная почта '), max_length=50, blank=True)
    position = models.ManyToManyField(Position, help_text="Должность человека")

    # def display_position(self):
    #     """
    #     Creates a string for the Genre. This is required to display genre in Admin.
    #     """
    #     return ', '.join([position.name for position in personal.position.all()[:4]])
    #
    # display_position().short_description = 'Должность'

    class Meta:
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персоналы'


class Rating(models.Model):
    """
    Модель рейтинга
    """
    id = models.OneToOneField(Company, on_delete=models.CASCADE, primary_key=True)
    rating = models.BigIntegerField(_('Рейтинг '), blank=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
