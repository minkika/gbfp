from django.urls import path

import companyapp.views as personalarea

app_name = 'company'

urlpatterns = [
    path('', personalarea.IndexView.as_view(), name='company_view'),
    path('update/<int:pk>', personalarea.CompanyUpdateView.as_view(), name='company_update'),
    path('detail/<int:pk>', personalarea.CompanyDetailView.as_view(), name='company_detail'),
]