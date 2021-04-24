from django.urls import path
from django.views.generic import TemplateView

import mainapp.views as mainapp

app_name = 'main'

urlpatterns = [
    path('invite/<int:pk>/', mainapp.invite, name='main_invite'),
    path('favorites/<int:pk>/', mainapp.favorites, name='main_favorites'),
    path('', mainapp.main_news, name='main'),
    path('list/', mainapp.vac_res_list, name='vac_res_list'),
]
