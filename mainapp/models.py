from django.db import models
from authapp.models import User
from vacancyapp.models import Vacancy
from resumeapp.models import Resume
# from django.utils.translation import gettext_lazy
# from django.core.exceptions import ValidationError


class BlogPost(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=50, null=False)
    text = models.TextField(verbose_name='Новость')
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)

    class Meta:
        verbose_name = 'новостной пост'
        verbose_name_plural = 'новостные посты'

    def __str__(self):
        return self.title


class Responses(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='Вакансия',
                                unique=False, null=True, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Резюме',
                               unique=False, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Кто откликнулся',
                             unique=False, null=False, blank=False)
    is_active = models.BooleanField(verbose_name='Активность', blank=False, default=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['vacancy', 'user'],
                                               name='unique_vacancy_user'),
                       models.UniqueConstraint(fields=['resume', 'user'],
                                               name='unique_resume_user')]

    # def validate_unique(self, exclude=None):
    #     try:
    #         super().validate_unique(exclude=exclude)
    #     except ValidationError:
    #         raise ValidationError(gettext_lazy('Такая запись уже существует.'))


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь',
                             unique=False, null=True, blank=False)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='Вакансия',
                                unique=False, null=True, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Резюме',
                               unique=False, null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Активность', blank=False, default=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['vacancy', 'user'],
                                               name='unique_favorites_vacancy_user'),
                       models.UniqueConstraint(fields=['resume', 'user'],
                                               name='unique_favorites_resume_user')]
