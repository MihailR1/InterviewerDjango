from django.contrib.postgres.indexes import GinIndex
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings import AUTH_USER_MODEL
from core.models import CommonDataAbstractModel
from core.slug import AutoSlugField


class Question(CommonDataAbstractModel):
    """Модель вопроса"""

    class ModerationStatus(models.TextChoices):
        """Enums со статусом модерации"""

        MODERATION = ("MODERATION", _("Модерация"))
        PUBLIC = ("PUBLIC", _("Опубликован"))
        DECLINED = ("DECLINED", _("Отклонен"))

    class LevelChoices(models.TextChoices):
        """Enums с уровнем вопроса Junior/middle/senior"""

        JUNIOR = ("JUNIOR", _("Junior"))
        MIDDLE = ("MIDDLE", _("Middle"))
        SENIOR = ("SENIOR", _("Senior"))

    user_id = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name=_("Пользователь"),
    )
    categories = models.ManyToManyField("Category", verbose_name=_("Категорий"))
    companies = models.ManyToManyField("companies.Company", verbose_name=_("В компаниях"))
    article = models.OneToOneField(
        "articles.Article",
        on_delete=models.CASCADE,
        verbose_name=_("Полный ответ"),
    )
    comments = models.ForeignKey(
        "comments.Comment",
        on_delete=models.CASCADE,
        verbose_name=_("Комментарии"),
    )
    title = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name=_("Заголовок")
    )
    text = models.TextField(unique=True, verbose_name=_("Текст вопроса"))
    answer = models.TextField(verbose_name=_("Ответ"))
    level = models.CharField(
        choices=LevelChoices,
        default=LevelChoices.JUNIOR,
        verbose_name=_("Для уровня"),
    )
    status = models.CharField(
        choices=ModerationStatus,
        default=ModerationStatus.MODERATION,
        verbose_name=_("Статус"),
    )
    slug = AutoSlugField(populate_from="title", unique=True, verbose_name=_("Ссылка"))

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")
        indexes = (GinIndex(fields=("text",)),)


class QuestionStat(CommonDataAbstractModel):
    """Статистика по вопросу"""

    question_id = models.OneToOneField(
        "Question", on_delete=models.CASCADE, verbose_name=_("Вопрос")
    )
    views = models.PositiveSmallIntegerField(verbose_name=_("Просмотров"))
    got_at_interview = models.PositiveSmallIntegerField(verbose_name=_("Встречался на интервью"))
    answers = models.ForeignKey(
        "attempts.Answer", on_delete=models.SET_NULL, null=True, verbose_name=_("Ответы")
    )

    class Meta:
        verbose_name = _("Статистика по вопросу")
        verbose_name_plural = _("Статистика по вопросу")


class Category(CommonDataAbstractModel):
    """Модель с категориями/тегами вопроса"""

    name = models.CharField(max_length=255, unique=True, verbose_name=_("Категория"))
    slug = AutoSlugField(populate_from="name", unique=True, verbose_name=_("Ссылка"))

    def questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name = _("Категории")
        verbose_name_plural = _("Категории")
