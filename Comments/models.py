from django.db import models

from Utils.models import CommonDataAbstractModel


class Comment(CommonDataAbstractModel):
    """Модель комментария к вопросу"""

    user_id = models.OneToOneField('User', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
