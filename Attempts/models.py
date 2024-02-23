from django.db import models
from django.utils.translation import gettext_lazy as _

from IntervDjango.settings import AUTH_USER_MODEL
from Utils.models import CommonDataAbstractModel


class Attempt(CommonDataAbstractModel):
    """Модель сессии из вопросов"""

    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    question_id = models.ForeignKey('Questions.Question', on_delete=models.SET_NULL, null=True, verbose_name='Вопросы')
    start_date = models.DateTimeField(auto_now_add=True, verbose_name='Время начала')
    end_date = models.DateTimeField(auto_now=True, verbose_name='Время завершения')
    answer = models.OneToOneField('Answer', on_delete=models.CASCADE,
                                  verbose_name='Оценил ответ')
    session_id = models.UUIDField(verbose_name='ID-Сессии')

    class Meta:
        verbose_name = 'Сессия интервью'
        verbose_name_plural = 'Сессии интервью'


class Answer(CommonDataAbstractModel):
    """Модель, как пользовать оценил свой ответ на вопрос"""

    class AnswerChoices(models.TextChoices):
        """Enums с вариантами оценки вопроса"""
        CORRECT = 'CORRECT', _('Верно')
        WRONG = 'WRONG', _('Не верно')
        MODERATE = 'MODERATE', _('Почти верно')

    answer = models.CharField(choices=AnswerChoices, default=AnswerChoices.CORRECT,
                              verbose_name='Оценил ответ')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
