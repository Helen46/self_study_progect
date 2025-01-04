# Generated by Django 5.1.4 on 2025-01-04 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Добавьте название курса', max_length=300, verbose_name='Название курса')),
                ('description', models.TextField(blank=True, help_text='Добавьте описание курса', null=True, verbose_name='Описание курса')),
                ('status', models.CharField(choices=[('available', 'доступен'), ('unavailable', 'недоступен'), ('in progress', 'в процессе'), ('passed', 'пройден')], default='available', max_length=16, verbose_name='Статус курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Добавьте название урока', max_length=300, verbose_name='Название урока')),
                ('lesson_content', models.TextField(help_text='Добавьте содержание урока', verbose_name='Содержание урока')),
                ('video', models.URLField(blank=True, help_text='Добавьте ссылку на видео урока', max_length=300, null=True, verbose_name='Ссылка на видео урока')),
                ('image', models.ImageField(blank=True, help_text='Добавьте изображение', null=True, upload_to='courses/images', verbose_name='Изображение')),
                ('status', models.CharField(choices=[('available', 'доступен'), ('unavailable', 'недоступен'), ('in progress', 'в процессе'), ('passed', 'пройден')], default='available', max_length=16, verbose_name='Статус урока')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
