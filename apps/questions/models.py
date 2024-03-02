from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _

from config.settings import AUTH_USER_MODEL
from core.enums import ModerationStatus
from core.models import SlugModel


class Question(SlugModel, TimeStampedModel, models.Model):
    """Модель вопроса"""

    class LevelChoices(models.TextChoices):
        """Enums с уровнем вопроса Junior/middle/senior"""

        JUNIOR = ("JUNIOR", _("Junior"))
        MIDDLE = ("MIDDLE", _("Middle"))
        SENIOR = ("SENIOR", _("Senior"))

    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default=1, verbose_name=_("Пользователь")
    )
    categories = models.ManyToManyField("Category", blank=True, verbose_name=_("Категорий"))
    companies = models.ManyToManyField(
        "companies.Company", blank=True, verbose_name=_("В компаниях")
    )
    article = models.OneToOneField(
        "articles.Article",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Полный ответ"),
    )
    comments = models.ForeignKey(
        "comments.Comment",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Комментарии"),
    )
    title = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name=_("Заголовок")
    )
    text = models.TextField(unique=True, db_index=True, verbose_name=_("Текст вопроса"))
    answer = models.TextField(verbose_name=_("Ответ"))
    level = models.CharField(
        choices=LevelChoices, default=LevelChoices.JUNIOR, verbose_name=_("Для уровня")
    )
    status = models.CharField(
        choices=ModerationStatus, default=ModerationStatus.MODERATION, verbose_name=_("Статус")
    )
    slug = AutoSlugField(populate_from="title", verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")

    def __str__(self) -> str:
        return self.title


class QuestionStat(TimeStampedModel, models.Model):
    """Статистика по вопросу"""

    question = models.OneToOneField("Question", on_delete=models.CASCADE, verbose_name=_("Вопрос"))
    views = models.PositiveSmallIntegerField(verbose_name=_("Просмотров"))
    got_at_interview = models.PositiveSmallIntegerField(verbose_name=_("Встречался на интервью"))
    answers = models.ForeignKey(
        "attempts.Answer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Ответы"),
    )

    class Meta:
        verbose_name = _("Статистика по вопросу")
        verbose_name_plural = _("Статистика по вопросу")


class Category(SlugModel, TimeStampedModel, models.Model):
    """Модель с категориями/тегами вопроса"""

    name = models.CharField(max_length=255, unique=True, verbose_name=_("Имя категории"))
    slug = AutoSlugField(populate_from="name", verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("Категории")
        verbose_name_plural = _("Категории")

    def questions(self) -> QuerySet:
        return self.question_set.all()

    def __str__(self) -> str:
        return self.name
