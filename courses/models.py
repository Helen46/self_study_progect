from django.db import models

from config.settings import NULLABLE, AUTH_USER_MODEL


STATUS_OF_PASSAGE = [
        ('available', 'доступен'),
        ('unavailable', 'недоступен'),
        ('in progress', 'в процессе'),
        ('passed', 'пройден')
    ]


class Course(models.Model):
    """
    Модель курса
    """
    name = models.CharField(
        max_length=300,
        verbose_name='Название курса',
        help_text='Добавьте название курса',
    )
    description = models.TextField(
        verbose_name='Описание курса',
        help_text='Добавьте описание курса',
        **NULLABLE
    )
    status = models.CharField(
        max_length=16,
        choices=STATUS_OF_PASSAGE,
        verbose_name='Статус курса',
        default='available'
    )
    autor = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор курса',
        **NULLABLE
    )
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    Модель урока
    """
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name='Курс',
        **NULLABLE
    )
    name = models.CharField(
        max_length=300,
        verbose_name='Название урока',
        help_text='Добавьте название урока',
    )
    lesson_content = models.TextField(
        verbose_name='Содержание урока',
        help_text='Добавьте содержание урока',
    )
    video = models.URLField(
        max_length=300,
        verbose_name='Ссылка на видео урока',
        help_text='Добавьте ссылку на видео урока',
        **NULLABLE
    )
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Изображение',
        help_text='Добавьте изображение',
        **NULLABLE
    )
    status = models.CharField(
        max_length=16,
        choices=STATUS_OF_PASSAGE,
        verbose_name='Статус урока',
        default='available'
    )
    autor = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор урока',
        **NULLABLE
    )
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name
