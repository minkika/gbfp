from django.contrib import admin

from mainapp.models import BlogPost


@admin.register(BlogPost)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
