"""gbfp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.generic import DetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('company/', include('companyapp.urls', namespace='company')),
    path('applicant/', include('applicantapp.urls', namespace='applicant')),
    path('vacancy/', include('vacancyapp.urls', namespace='vacancy')),
    path('rules/', TemplateView.as_view(template_name='mainapp/rules.html'), name='rules'),
    path('', include('mainapp.urls', namespace='main')),
    path('resume/', include('resumeapp.urls', namespace='resume')),
    ]
