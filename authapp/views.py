from django.conf import settings
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import auth
from django.views.generic import CreateView

from authapp.forms import UserLoginForm, ApplicantRegistrationForm, CompanyRegistrationForm
from authapp.models import User


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user: {e.args}')
        return HttpResponseRedirect(reverse('main:main'))


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'

    message = f'Для подтверждения учетной записи {user.username} на сайте GB группы 2/2' \
              f'перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    # print(message)

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


class Login(LoginView):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:main'))


class ApplicantRegistration(CreateView):
    form_class = ApplicantRegistrationForm
    success_url = reverse_lazy('auth:login')
    template_name = 'authapp/register.html'

    def form_valid(self, form):
        if self.request.method == 'POST':
            register_form = ApplicantRegistrationForm(self.request.POST, self.request.FILES)
            if register_form.is_valid():
                user = register_form.save()
                if send_verify_mail(user):
                    print('email sending success')
                else:
                    print('error while email sending')
                return HttpResponseRedirect(reverse('auth:login'))
        else:
            register_form = ApplicantRegistrationForm()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['reg_type'] = self.kwargs['reg_type']
    #     return context


class CompanyRegistration(CreateView):
    form_class = CompanyRegistrationForm
    success_url = reverse_lazy('auth:login')
    template_name = 'authapp/register.html'

    def form_valid(self, form):
        if self.request.method == 'POST':
            register_form = CompanyRegistrationForm(self.request.POST, self.request.FILES)
            if register_form.is_valid():
                obj = register_form.save()
                obj.is_staff = True
                user = register_form.save()
                if send_verify_mail(user):
                    print('email sending success')
                else:
                    print('error while email sending')
                return HttpResponseRedirect(reverse('auth:login'))
        else:
            register_form = CompanyRegistrationForm()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['reg_type'] = self.kwargs['reg_type']
    #     return context

# def register(request, reg_type='applicant'):
#     title = 'Регистрация соискателя' if reg_type == 'applicant' else 'Регистрация работодателя'
#
#     if reg_type == 'company':
#         form = CompanyRegistrationForm(data=request.POST)
#     else:
#         form = ApplicantRegistrationForm(data=request.POST)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             user = form.save()
#             if reg_type == 'company':
#                 user.is_staff = True
#                 user.save()
#             return HttpResponseRedirect(reverse('auth:login'))
#     else:
#         if reg_type == 'company':
#             form = CompanyRegistrationForm(data=request.POST)
#         else:
#             form = ApplicantRegistrationForm(data=request.POST)
#
#     content = {
#         'title': title,
#         'form': form,
#         'reg_type': reg_type
#     }
#     return render(request, 'registration/register.html', content)

