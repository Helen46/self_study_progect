from django.db import models

from config.settings import NULLABLE


class Course(models.Model):
    """
    Модель курса
    """
    STATUS_OF_PASSAGE = [
        ('available', 'доступен'),
        ('unavailable', 'недоступен'),
        ('in progress', 'в процессе'),
        ('passed', 'пройден')
    ]
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
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name
