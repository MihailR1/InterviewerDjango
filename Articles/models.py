from django.db import models

from IntervDjango.settings import AUTH_USER_MODEL
from Utils.models import CommonDataAbstractModel
from Utils.slug import AutoSlugField


class Article(CommonDataAbstractModel):
    """Статья с полным разбором вопроса"""
    user_id = models.ForeignKey(AUTH_USER_MODEL, models.SET_DEFAULT,
                                default=1, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Полный текст ответа')
    slug = AutoSlugField(populate_from='text', unique=True, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
