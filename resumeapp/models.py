from django.db import models
from authapp.models import User


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    resume_name = models.CharField(verbose_name='Желаемая должность', max_length=250, blank=True, null=True)
    cellphone = models.PositiveBigIntegerField(verbose_name='Номер телефона')
    salary = models.FloatField(verbose_name='Ожидаемая заработная плата', blank=True, default=0)
    education = models.TextField(verbose_name='Образование', blank=True, default='')
    job_list = models.TextField(verbose_name='Опыт работы', blank=True, default='')
    key_words = models.TextField(verbose_name='Ключевы навыки', blank=True, default='')
    languages = models.TextField(verbose_name='Знание языков', blank=True, default='')
    is_draft = models.BooleanField(verbose_name='Черновик', default=False)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)
    is_active = models.BooleanField(verbose_name='Опубликовано', default=False)
    is_approved = models.BooleanField(verbose_name='Проверено', default=False)

    class Meta:
        ordering = ('resume_name',)
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return f'{self.resume_name} ({self.salary})'
