from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.indexes import HashIndex
from django.db import models

from Utils.models import CommonDataAbstractModel


class User(AbstractUser):
    """Модель пользователя"""

    class Meta:
        indexes = (HashIndex(fields=('email',)),)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'


class Profile(CommonDataAbstractModel):
    """Модель с настройками аккаунта пользователя"""

    user_id = models.OneToOneField('User', on_delete=models.CASCADE)
    remind_in = models.PositiveSmallIntegerField(default=2, help_text='Напоминать о тренировках раз в N дня')
    remind_easy = models.PositiveSmallIntegerField(default=6)
    remind_difficult = models.PositiveSmallIntegerField(default=1)
    remind_moderate = models.PositiveSmallIntegerField(default=3)

    class Meta:
        verbose_name = 'Настройки пользователя'
        verbose_name_plural = 'Настройки пользователя'


class Favorite(CommonDataAbstractModel):
    """Модель для добавления избранных вопросов"""

    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    question_id = models.ForeignKey('Questions.Question', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'


class Review(CommonDataAbstractModel):
    """Модель отзыва пользователем о нашем сервисе"""

    user_id = models.OneToOneField('User', on_delete=models.CASCADE)
    text = models.TextField()
    number_of_interview_sessions = models.IntegerField()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
