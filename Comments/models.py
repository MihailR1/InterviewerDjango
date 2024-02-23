from django.db import models

from IntervDjango.settings import AUTH_USER_MODEL
from Utils.models import CommonDataAbstractModel


class Comment(CommonDataAbstractModel):
    """Модель комментария к вопросу"""

    user_id = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
