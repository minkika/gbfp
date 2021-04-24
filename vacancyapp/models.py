from django.db import models
from authapp.models import User


class Vacancy(models.Model):
    company = models.ForeignKey(User, verbose_name='Компания', blank=True, null=True, on_delete=models.SET_NULL)
    vacancy_name = models.CharField(verbose_name='Наименование должности', max_length=250, blank=True, null=True)
    description = models.TextField(verbose_name='Описание должности', max_length=250, blank=True, null=True)
    salary = models.FloatField(verbose_name='Заработная плата', blank=True, default=0)
    is_draft = models.BooleanField(verbose_name='Черновик', default=False)
    is_active = models.BooleanField(verbose_name='Опубликовано', default=False)
    created_at = models.DateTimeField(verbose_name='Создана', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлена', auto_now=True)

    is_approved = models.BooleanField(verbose_name='Проверено', default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.vacancy_name
