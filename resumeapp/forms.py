from django import forms
from django.forms.fields import BooleanField

from resumeapp.models import Resume


class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('is_active', 'user', 'is_approved',)

    def __init__(self, *args, **kwargs):
        super(ResumeEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field) != BooleanField:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''


class ResumeSearchForm(forms.Form):
    salary_min = forms.FloatField(required=False, label='ЗП от',
                                  widget=forms.TextInput(attrs={'placeholder': 'зарплата от'}))
    salary_max = forms.FloatField(required=False, label='ЗП до',
                                  widget=forms.TextInput(attrs={'placeholder': 'зарплата до'}))
    resume_name = forms.CharField(required=False, label='Название резюме',
                                  widget=forms.TextInput(attrs={'placeholder': 'Название резюме'}))

    def __init__(self, *args, **kwargs):
        super(ResumeSearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field) != BooleanField:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
