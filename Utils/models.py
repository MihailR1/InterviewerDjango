from django.db import models


class CommonDataAbstractModel(models.Model):
    """Абстрактная модель с частыми полями,
    которые нужны при создании моделей"""

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.id}'
