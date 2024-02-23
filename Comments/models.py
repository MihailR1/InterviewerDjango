from django.db import models

from IntervDjango.settings import AUTH_USER_MODEL
from Utils.models import CommonDataAbstractModel


class Comment(CommonDataAbstractModel):
    """Модель комментария к вопросу"""

    user_id = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
