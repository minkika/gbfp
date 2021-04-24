from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse
from applicantapp.forms import ApplicantEditForm
from authapp.models import User
from resumeapp.models import Resume
from mainapp.models import Responses, Favorites


class IndexView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'applicantapp/applicant_content.html'
    model = Resume

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['resume_list'] = Resume.objects.filter(user_id=self.request.user.pk)
        responses = Responses.objects.filter(resume_id__in=
                                             Resume.objects.filter(user_id=
                                                                   self.request.user.pk), is_active=True).order_by('user')
        favorites = Favorites.objects.filter(user_id=self.request.user.pk, is_active=True)
        context['favorites'] = favorites
        context['responses_list'] = responses
        context['title'] = 'Личный кабинет соискателя'
        return context

    def test_func(self):
        return not self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main'))


class ApplicantUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    success_url = reverse_lazy('applicant:applicant_view')
    form_class = ApplicantEditForm
    title = 'Редактировать данные профиля'
    template_name = 'applicantapp/applicant_form.html'

    def test_func(self):
        return self.request.user.pk == self.kwargs['pk']

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main'))


class ApplicantDetailView(DetailView):
    model = User
    title = 'Соискатель'
    template_name = 'applicantapp/applicant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ApplicantDetailView, self).get_context_data(**kwargs)
        context['resume_list'] = Resume.objects.filter(user_id=self.kwargs['pk'], is_active=True)
        return context
