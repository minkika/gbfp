from django.urls import path

import applicantapp.views as applicant

app_name = 'applicant'

urlpatterns = [
    path('', applicant.IndexView.as_view(), name='applicant_view'),
    path('update/<int:pk>', applicant.ApplicantUpdateView.as_view(), name='applicant_update'),
    path('detail/<int:pk>', applicant.ApplicantDetailView.as_view(), name='applicant_detail'),
]