from django import forms
from django.forms.fields import BooleanField

from vacancyapp.models import Vacancy


class VacancyEditForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ('is_active', 'company', 'is_approved', 'is_approved',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field) != BooleanField:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''


class VacancySearchForm(forms.Form):
    salary_min = forms.FloatField(required=False, label='ЗП от',
                                  widget=forms.TextInput(attrs={'placeholder': 'зарплата от'}))
    salary_max = forms.FloatField(required=False, label='ЗП до',
                                  widget=forms.TextInput(attrs={'placeholder': 'зарплата до'}))
    vacancy_name = forms.CharField(required=False, label='Название вакансии',
                                   widget=forms.TextInput(attrs={'placeholder': 'Название вакансии'}))
    company = forms.CharField(required=False, label='Название компании',
                              widget=forms.TextInput(attrs={'placeholder': 'Название компании'}))

    def __init__(self, *args, **kwargs):
        super(VacancySearchForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if type(field) != BooleanField:
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''
