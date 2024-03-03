from ckeditor.fields import RichTextField
from django_extensions.db.models import TimeStampedModel

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.indexes import HashIndex
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.manager import CustomUserManager
from config.config import settings
from config.settings import AUTH_USER_MODEL
from core.enums import ModerationStatus


class User(TimeStampedModel, AbstractUser):
    """Модель пользователя"""

    email = models.EmailField("email address", unique=True)

    objects = CustomUserManager()

    class Meta:
        indexes = (HashIndex(fields=("email",)),)
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self) -> str:
        return self.email


class Profile(TimeStampedModel, models.Model):
    """Модель с настройками аккаунта пользователя"""

    user = models.OneToOneField(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    remind_in = models.PositiveSmallIntegerField(
        default=2, verbose_name=_("Напоминать о тренировках")
    )
    remind_easy = models.PositiveSmallIntegerField(default=6, verbose_name=_("Верно"))
    remind_difficult = models.PositiveSmallIntegerField(default=1, verbose_name=_("Не верно"))
    remind_moderate = models.PositiveSmallIntegerField(default=3, verbose_name=_("Не совсем верно"))

    class Meta:
        verbose_name = _("Настройки пользователя")
        verbose_name_plural = _("Настройки пользователя")


class Favorite(TimeStampedModel, models.Model):
    """Модель для добавления избранных вопросов"""

    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    question = models.ForeignKey(
        "questions.Question",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_("Вопросы"),
    )

    class Meta:
        verbose_name = _("Избранное")
        verbose_name_plural = _("Избранные")


class Review(TimeStampedModel, models.Model):
    """Модель отзыва пользователем о нашем сервисе"""

    user = models.OneToOneField(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    text = models.TextField(verbose_name=_("Текст отзыва"))
    number_of_interview_sessions = models.PositiveSmallIntegerField(verbose_name=_("Кол-во сессий"))
    status = models.CharField(
        choices=ModerationStatus, default=ModerationStatus.MODERATION, verbose_name=_("Статус")
    )

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")

    def __str__(self) -> str:
        return self.text[: settings.admin_preview_text]
