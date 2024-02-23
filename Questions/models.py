from django.db import models
from django.utils.translation import gettext_lazy as _

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

    user_id = models.ForeignKey('Accounts.User', on_delete=models.SET_NULL)
    categories = models.ManyToManyField('Category')
    companies = models.ManyToManyField('Companies.Company')
    article = models.OneToOneField('Articles.Article', on_delete=models.CASCADE)
    comments = models.ForeignKey('Comments.Comment', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    text = models.TextField(unique=True)
    answer = models.TextField()
    level = models.CharField(choices=LevelChoices, default=LevelChoices.JUNIOR)
    status = models.CharField(choices=ModerationStatus, default=ModerationStatus.MODERATION)
    slug = AutoSlugField(populate_from='title', unique=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class QuestionStat(CommonDataAbstractModel):
    """Статистика по вопросу"""

    question_id = models.OneToOneField('Question', on_delete=models.CASCADE)
    views = models.IntegerField()
    got_at_interview = models.IntegerField()
    answers = models.ForeignKey('Attempts.Answer', on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Статистика по вопросу'
        verbose_name_plural = 'Статистика по вопросу'


class Category(CommonDataAbstractModel):
    """Модель с категориями/тегами вопроса"""

    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

