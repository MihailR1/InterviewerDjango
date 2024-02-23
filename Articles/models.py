from django.db import models

from Utils.models import CommonDataAbstractModel
from Utils.slug import AutoSlugField


class Article(CommonDataAbstractModel):
    """Статья с полным разбором вопроса"""
    user_id = models.ForeignKey('Accounts.User', models.SET_NULL, verbose_name='Пользователь')
    text = models.TextField()
    slug = AutoSlugField(populate_from='text', unique=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
