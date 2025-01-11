from django.db import models

from config.settings import NULLABLE, AUTH_USER_MODEL
from courses.models import Course, Lesson


class Test(models.Model):
    """
    Модель теста для пользователя
    """
    name = models.CharField(
        max_length=150,
        verbose_name='Название тест',
        help_text='Введите название теста'
    )
    body = models.TextField(
        verbose_name='Инструкция к тесту',
        help_text='Добавьте инструкцию к тесту',
        **NULLABLE
    )
    autor = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор теста',
        **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс, к которому относится тест',
        help_text='Выберите курс, к которому относится тест',
        **NULLABLE
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='Урок, к которому относится тест',
        help_text='Выберите урок, к которому относится тест',
        **NULLABLE
    )
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    Модель вопроса
    """
    name = models.TextField(
        verbose_name='Текст вопроса',
        help_text='Введите текст вопроса',
    )
    image = models.ImageField(
        upload_to='users_tests/images',
        verbose_name='Изображение',
        help_text='Добавьте изображение',
        **NULLABLE
    )
    test = models.ManyToManyField(
        Test,
        verbose_name='Тест',
        help_text='Укажите для какого теста этот вопрос',
    )
    autor = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор вопроса',
        **NULLABLE
    )
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.name


class Answer(models.Model):
    """
    Модель ответа
    """
    name = models.TextField(
        verbose_name='Текст ответа',
        help_text='Введите текст ответа',
    )
    image = models.ImageField(
        upload_to='users_tests/images',
        verbose_name='Изображение',
        help_text='Добавьте изображение',
        **NULLABLE
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Ответ на вопрос',
        help_text='Укажите для какого вопроса этот ответ',
        **NULLABLE
    )
    is_correct = models.BooleanField(
        default=False,
        verbose_name='Правильность ответа',
        help_text='Отметьте, если ответ правильный',
        **NULLABLE
    )
    autor = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор ответа',
        **NULLABLE
    )
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.name
