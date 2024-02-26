from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.indexes import HashIndex
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings import AUTH_USER_MODEL
from core.models import CommonDataAbstractModel


class User(AbstractUser):
    """Модель пользователя"""

    email = models.EmailField("email address", unique=True)

    class Meta:
        indexes = (HashIndex(fields=("email",)),)
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return f"{self.email}"


class Profile(CommonDataAbstractModel):
    """Модель с настройками аккаунта пользователя"""

    user_id = models.OneToOneField(
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


class Favorite(CommonDataAbstractModel):
    """Модель для добавления избранных вопросов"""

    user_id = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    question_id = models.ForeignKey(
        "questions.Question",
        on_delete=models.CASCADE,
        verbose_name=_("Вопросы"),
    )

    class Meta:
        verbose_name = _("Избранное")
        verbose_name_plural = _("Избранные")


class Review(CommonDataAbstractModel):
    """Модель отзыва пользователем о нашем сервисе"""

    user_id = models.OneToOneField(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    text = models.TextField(verbose_name=_("Текст отзыва"))
    number_of_interview_sessions = models.PositiveSmallIntegerField(verbose_name=_("Кол-во сессий"))

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")
