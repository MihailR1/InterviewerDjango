from django.db import models
from django.utils.translation import gettext_lazy as _

from config.settings import AUTH_USER_MODEL
from core.models import CommonDataAbstractModel


class Attempt(CommonDataAbstractModel):
    """Модель сессии из вопросов"""

    user_id = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Пользователь"),
    )
    question_id = models.ForeignKey(
        "questions.Question", on_delete=models.SET_NULL, null=True, verbose_name=_("Вопросы")
    )
    start_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Время начала"))
    end_date = models.DateTimeField(auto_now=True, verbose_name=_("Время завершения"))
    answer = models.OneToOneField(
        "Answer", on_delete=models.CASCADE, verbose_name=_("Оценил ответ")
    )
    session_id = models.UUIDField(verbose_name=_("ID-Сессии"))

    class Meta:
        verbose_name = _("Сессия интервью")
        verbose_name_plural = _("Сессии интервью")


class Answer(CommonDataAbstractModel):
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
