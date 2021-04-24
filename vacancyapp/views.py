from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from mainapp.models import Responses, Favorites
from vacancyapp.forms import VacancyEditForm
from vacancyapp.models import Vacancy
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404


class VacancyListView(ListView):
    model = Vacancy
    paginate_by = 10
    title = 'Вакансии'
    ordering = '-is_active'
    template_name = 'companyapp/pa_content.html'


class VacancyDetailView(DetailView):
    model = Vacancy
    title = 'Вакансия'
    template_name = 'vacancyapp/vacancy_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_responses'] = False
        context['in_favorites'] = False
        response = Responses.objects.filter(vacancy_id=self.kwargs['pk'], user_id=self.request.user.pk, is_active=True)
        favorites = Favorites.objects.filter(vacancy_id=self.kwargs['pk'], user_id=self.request.user.pk, is_active=True)
        if response:
            context['in_responses'] = True
        if favorites:
            context['in_favorites'] = True
        return context


class VacancyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vacancy
    success_url = reverse_lazy('company:company_view')
    form_class = VacancyEditForm
    title = 'Создать вакансию'
    template_name = 'vacancyapp/vacancy_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user
        return super(VacancyCreateView, self).form_valid(form)

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main'))


class VacancyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vacancy
    success_url = reverse_lazy('company:company_view')
    form_class = VacancyEditForm
    title = 'Редактировать вакансию'
    template_name = 'vacancyapp/vacancy_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user
        return super(VacancyUpdateView, self).form_valid(form)

    def test_func(self):
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        result = obj.company == self.request.user and self.request.user.is_staff
        return result

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main'))


class VacancyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vacancy
    success_url = reverse_lazy('company:company_view')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
        else:
            self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    def test_func(self):
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        result = obj.company == self.request.user and self.request.user.is_staff
        return result

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main'))

