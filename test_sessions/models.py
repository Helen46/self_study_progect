from django.db import models

from config.settings import NULLABLE, AUTH_USER_MODEL
from users.models import User
from users_tests.models import Test, Question


class TestSession(models.Model):
    """
    Модель сессии теста
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        **NULLABLE
    )
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        verbose_name='Тест',
        **NULLABLE
    )
    class Meta:
        verbose_name = 'Сессия теста'
        verbose_name_plural = 'Сессии тестов'


class UserAnswer(models.Model):
    """
    Модель ответа пользователя
    """
    session = models.ForeignKey(
        TestSession,
        on_delete=models.CASCADE,
        **NULLABLE
    )
    body = models.CharField(
        max_length=300,
        verbose_name='Ответ пользователя'
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        **NULLABLE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='На какой вопрос этот ответ'
    )
    attempt = models.IntegerField(
        default=0,
        verbose_name='Номер попытки'
    )
    is_correct = models.BooleanField(
        verbose_name='Правильность ответа',
        **NULLABLE
    )
    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'

    def __str__(self):
        return self.body

