from django.contrib import admin

from resumeapp.models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('resume_name', 'user', 'is_draft', 'is_approved', 'is_active')
    list_display_links = ('user', 'resume_name')
    list_filter = ('is_draft', 'is_active', 'is_approved')

    def published(self, obj):
        return not Resume.objects.filter(user__resume=obj).first().is_draft
    published.short_description = 'Опубликовано'
    published.boolean = True
