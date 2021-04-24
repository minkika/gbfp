from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from vacancyapp.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('vacancy_name', 'company', 'is_draft', 'is_approved', 'is_active')
    list_display_links = ('vacancy_name', 'company')
    list_filter = ('is_draft', 'is_active', 'is_approved')

    def published(self, obj):
        return not Vacancy.objects.filter(company__vacancy=obj).first().is_draft
    published.short_description = 'Опубликовано'
    published.boolean = True

