# Generated by Django 3.2.16 on 2024-03-02 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('start_date', models.DateTimeField(verbose_name='Дата старта курса')),
                ('price', models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Стоимость курса')),
                ('min_group_users', models.PositiveIntegerField(default=10, verbose_name='Минимальное количество учеников в группе')),
                ('max_group_users', models.PositiveIntegerField(default=30, verbose_name='Максимальное количество учеников в группе')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_created', to=settings.AUTH_USER_MODEL, verbose_name='Автор курса')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название урока')),
                ('video_link', models.URLField(verbose_name='Ссылка на видео')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='products.course', verbose_name='Урок')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название группы')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='products.course', verbose_name='Курс')),
                ('users', models.ManyToManyField(related_name='group_memberships', to=settings.AUTH_USER_MODEL, verbose_name='Участники группы')),
            ],
        ),
    ]