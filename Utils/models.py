from django.db import models


class CommonDataAbstractModel(models.Model):
    """Абстрактная модель с частыми полями,
    которые нужно при создании моделей"""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.id}'
