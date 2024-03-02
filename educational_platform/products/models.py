from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='courses_created',
        verbose_name='Автор курса'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Название курса'
    )
    start_date = models.DateTimeField(verbose_name='Дата старта курса')
    price = models.DecimalField(
        max_digits=7,
        decimal_places=0,
        verbose_name='Стоимость курса'
    )
    min_group_users = models.PositiveIntegerField(
        default=10,
        verbose_name='Минимальное количество учеников в группе'
    )
    max_group_users = models.PositiveIntegerField(
        default=30,
        verbose_name='Максимальное количество учеников в группе'
    )

    def __str__(self):
        return self.title


class Lesson(models.Model):
    product = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Урок'
    )
    title = models.CharField(max_length=256, verbose_name='Название урока')
    video_link = models.URLField(verbose_name='Ссылка на видео')

    def __str__(self):
        return self.title


class Group(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Курс'
    )
    name = models.CharField(max_length=100, verbose_name='Название группы')
    users = models.ManyToManyField(
        User,
        related_name='group_memberships',
        verbose_name='Участники группы'
    )

    def __str__(self):
        return self.name
