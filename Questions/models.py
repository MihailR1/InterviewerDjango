from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _

from IntervDjango.settings import AUTH_USER_MODEL
from Utils.models import CommonDataAbstractModel
from Utils.slug import AutoSlugField


class Question(CommonDataAbstractModel):
    """Модель вопроса"""

    class ModerationStatus(models.TextChoices):
        """Enums со статусом модерации"""
        MODERATION = 'MODERATION', _('Модерация')
        PUBLIC = 'PUBLIC', _('Опубликован')
        DECLINED = 'DECLINED', _('Отклонен')

    class LevelChoices(models.TextChoices):
        """Enums с уровнем вопроса Junior/middle/senior"""
        JUNIOR = 'JUNIOR', _('Junior')
        MIDDLE = 'MIDDLE', _('Middle')
        SENIOR = 'SENIOR', _('Senior')

    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1,
                                verbose_name='Пользователь')
    categories = models.ManyToManyField('Category', verbose_name='Категорий')
    companies = models.ManyToManyField('Companies.Company', verbose_name='В компаниях')
    article = models.OneToOneField('Articles.Article', on_delete=models.CASCADE,
                                   verbose_name='Полный ответ')
    comments = models.ForeignKey('Comments.Comment', on_delete=models.CASCADE,
                                 verbose_name='Комментарии')
    title = models.CharField(max_length=255, unique=True, db_index=True, verbose_name='Заголовок')
    text = models.TextField(unique=True, verbose_name='Текст вопроса')
    answer = models.TextField(verbose_name='Ответ')
    level = models.CharField(choices=LevelChoices, default=LevelChoices.JUNIOR, verbose_name='Для уровня')
    status = models.CharField(choices=ModerationStatus, default=ModerationStatus.MODERATION, verbose_name='Статус')
    slug = AutoSlugField(populate_from='title', unique=True, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        indexes = (GinIndex(fields=('text',)),)


class QuestionStat(CommonDataAbstractModel):
    """Статистика по вопросу"""

    question_id = models.OneToOneField('Question', on_delete=models.CASCADE, verbose_name='Вопрос')
    views = models.PositiveSmallIntegerField(verbose_name='Просмотров')
    got_at_interview = models.PositiveSmallIntegerField(verbose_name='Встречался на интервью')
    answers = models.ForeignKey('Attempts.Answer', on_delete=models.SET_NULL, null=True, verbose_name='Ответы')

    class Meta:
        verbose_name = 'Статистика по вопросу'
        verbose_name_plural = 'Статистика по вопросу'


class Category(CommonDataAbstractModel):
    """Модель с категориями/тегами вопроса"""

    name = models.CharField(max_length=255, unique=True, verbose_name='Категория')
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name='Ссылка')

    def questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
