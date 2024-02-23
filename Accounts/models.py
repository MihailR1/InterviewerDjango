from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.indexes import HashIndex
from django.db import models

from IntervDjango.settings import AUTH_USER_MODEL
from Utils.models import CommonDataAbstractModel


class User(AbstractUser):
    """Модель пользователя"""

    email = models.EmailField('email address', unique=True)

    class Meta:
        indexes = (HashIndex(fields=('email',)),)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'


class Profile(CommonDataAbstractModel):
    """Модель с настройками аккаунта пользователя"""

    user_id = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   verbose_name='Пользователь')
    remind_in = models.PositiveSmallIntegerField(default=2,
                                                 verbose_name='Напоминать о тренировках')
    remind_easy = models.PositiveSmallIntegerField(default=6, verbose_name='Верно')
    remind_difficult = models.PositiveSmallIntegerField(default=1, verbose_name='Не верно')
    remind_moderate = models.PositiveSmallIntegerField(default=3, verbose_name='Не совсем верно')

    class Meta:
        verbose_name = 'Настройки пользователя'
        verbose_name_plural = 'Настройки пользователя'


class Favorite(CommonDataAbstractModel):
    """Модель для добавления избранных вопросов"""

    user_id = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    question_id = models.ForeignKey('Questions.Question', on_delete=models.CASCADE, verbose_name='Вопросы')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'


class Review(CommonDataAbstractModel):
    """Модель отзыва пользователем о нашем сервисе"""

    user_id = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст отзыва')
    number_of_interview_sessions = models.PositiveSmallIntegerField(verbose_name='Кол-во сессий')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
