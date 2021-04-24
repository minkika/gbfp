from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from mainapp.models import Responses, Favorites
from resumeapp.forms import ResumeEditForm
from resumeapp.models import Resume
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404


class ResumeListView(ListView):
    model = Resume
    paginate_by = 10
    title = 'Резюме'
    ordering = '-is_active'
    template_name = 'resumeapp/resume_list.html'


class ResumeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Resume
    success_url = reverse_lazy('applicant:applicant_view')
    form_class = ResumeEditForm
    title = 'Создать резюме'
    template_name = 'resumeapp/resume_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ResumeCreateView, self).form_valid(form)

    def test_func(self):
        return not self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main'))


class ResumeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resume
    exclude = ('is_approved',)
    success_url = reverse_lazy('applicant:applicant_view')
    form_class = ResumeEditForm
    title = 'Редактировать резюме'
    template_name = 'resumeapp/resume_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.company = self.request.user
        return super(ResumeUpdateView, self).form_valid(form)

    def test_func(self):
        obj = get_object_or_404(self.model, pk=self.kwargs['pk'])
        result = obj.user == self.request.user and not self.request.user.is_staff
        return result

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main'))


class ResumeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resume
    success_url = reverse_lazy('applicant:applicant_view')

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
        result = obj.user == self.request.user and not self.request.user.is_staff
        return result

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('main:main'))


class ResumeDetailView(DetailView):
    model = Resume
    title = 'Вакансия'
    exclude = ('is_approved',)
    template_name = 'resumeapp/resume_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['in_responses'] = False
        context['in_favorites'] = False
        response = Responses.objects.filter(resume_id=self.kwargs['pk'], user_id=self.request.user.pk, is_active=True)
        favorites = Favorites.objects.filter(resume_id=self.kwargs['pk'], user_id=self.request.user.pk, is_active=True)
        if response:
            context['in_responses'] = True
        if favorites:
            context['in_favorites'] = True
        return context
