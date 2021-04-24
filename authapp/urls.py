from django.conf.urls import url
from django.urls import path, include, re_path

import authapp.views as authapp

app_name = 'auth'

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('login/', authapp.login, name='login'),
    path('login/', authapp.Login.as_view(extra_context={'title': 'Авторизация'}), name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/applicant',
         authapp.ApplicantRegistration.as_view(extra_context={'title': 'Регистрация', 'reg_type': 'applicant'}),
         name='register_applicant'),
    path('register/company',
         authapp.CompanyRegistration.as_view(extra_context={'title': 'Регистрация', 'reg_type': 'company'}),
         name='register_company'),

    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),

]
