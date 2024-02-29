from django_extensions.db.models import TimeStampedModel

from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings import AUTH_USER_MODEL


class Attempt(TimeStampedModel, models.Model):
    """Модель сессии из вопросов"""

    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Пользователь")
    )
    question = models.ForeignKey(
        "questions.Question",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Вопросы"),
    )
    start_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Время начала"))
    end_date = models.DateTimeField(auto_now=True, verbose_name=_("Время завершения"))
    answer = models.OneToOneField(
        "Answer", null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("Оценил ответ")
    )
    session_id = models.UUIDField(verbose_name=_("ID-Сессии"))

    class Meta:
        verbose_name = _("Сессия интервью")
        verbose_name_plural = _("Сессии интервью")

    def __str__(self) -> str:
        return f"Session ID: {self.session_id}"


class Answer(TimeStampedModel, models.Model):
    """Модель, как пользовать оценил свой ответ на вопрос"""

    class AnswerChoices(models.TextChoices):
        """Enums с вариантами оценки вопроса"""

        CORRECT = ("CORRECT", _("Верно"))
        WRONG = ("WRONG", _("Не верно"))
        MODERATE = ("MODERATE", _("Почти верно"))

    answer = models.CharField(
        choices=AnswerChoices, default=AnswerChoices.CORRECT, verbose_name=_("Оценил ответ")
    )

    class Meta:
        verbose_name = _("Ответ")
        verbose_name_plural = _("Ответы")

    def __str__(self) -> str:
        return self.answer
