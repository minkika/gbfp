from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from mainapp.models import BlogPost, Favorites
from authapp.models import User
from resumeapp.forms import ResumeSearchForm
from vacancyapp.forms import VacancySearchForm
from vacancyapp.models import Vacancy
from resumeapp.models import Resume
from mainapp.models import Responses
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


def main_news(request):
    blog_posts = BlogPost.objects.all()

    paginator = Paginator(blog_posts, 5)
    page = request.GET.get('page', 1)

    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        blog_posts = paginator.page(1)
    except EmptyPage:
        blog_posts = paginator.page(paginator.num_pages)

    company_list = User.objects.filter(is_partner=True, is_superuser=False)
    context = {
        'blog_posts': blog_posts,
        'company_list': company_list,
        'paginator': paginator
    }
    return render(request, 'mainapp/main.html', context)


def vac_res_list(request):
    if request.user.is_staff:
        form = ResumeSearchForm
        data = Resume.objects.filter(is_draft=False, is_active=True, is_approved=True)
        if request.GET.get('salary_min'):
            data = data.filter(salary__gte=request.GET.get('salary_min'))
        if request.GET.get('salary_max'):
            data = data.filter(salary__lte=request.GET.get('salary_max'))
        if request.GET.get('resume_name'):
            data = data.filter(resume_name__contains=request.GET.get('resume_name'))
        title = 'Список резюме'
    else:
        form = VacancySearchForm
        data = Vacancy.objects.filter(is_draft=False, is_active=True, is_approved=True)
        if request.GET.get('salary_min'):
            data = data.filter(salary__gte=request.GET.get('salary_min'))
        if request.GET.get('salary_max'):
            data = data.filter(salary__lte=request.GET.get('salary_max'))
        if request.GET.get('vacancy_name'):
            data = data.filter(vacancy_name__contains=request.GET.get('vacancy_name'))
        if request.GET.get('company'):
            data = data.filter(company__company_name__contains=request.GET.get('company'))
        title = 'Список вакансий'
    page = request.GET.get('page')
    paginator = Paginator(data, 5)
    try:
        data_paginator = paginator.page(page)
    except PageNotAnInteger:
        data_paginator = paginator.page(1)
    except EmptyPage:
        data_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'page': page,
        'data': data_paginator,
        'form': form,
    }
    return render(request, 'mainapp/vacancy_list.html', context)


def invite(request, pk):
    if request.user.is_staff:
        resume = Resume.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        try:
            check = Responses.objects.get(resume=resume,
                                          user=user)
        except ObjectDoesNotExist:
            Responses.objects.create(resume=resume,
                                     user=user)
        else:
            if not check.is_active:
                check.is_active = True
                check.save()
            else:
                check.is_active = False
                check.save()
    else:
        vacancy = Vacancy.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        try:
            check = Responses.objects.get(vacancy=vacancy,
                                          user=user)
        except ObjectDoesNotExist:
            Responses.objects.create(vacancy=vacancy,
                                     user=user)
        else:
            if not check.is_active:
                check.is_active = True
                check.save()
            else:
                check.is_active = False
                check.save()
    return redirect(request.META['HTTP_REFERER'])


def favorites(request, pk):
    if request.user.is_staff:
        resume = Resume.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        try:
            check = Favorites.objects.get(resume=resume,
                                          user=user)
        except ObjectDoesNotExist:
            Favorites.objects.create(resume=resume,
                                     user=user)
        else:
            if not check.is_active:
                check.is_active = True
                check.save()
            else:
                check.is_active = False
                check.save()

    else:
        vacancy = Vacancy.objects.filter(pk=pk).first()
        user = User.objects.filter(pk=request.user.pk).first()
        try:
            check = Favorites.objects.get(vacancy=vacancy,
                                          user=user)
        except ObjectDoesNotExist:
            Favorites.objects.create(vacancy=vacancy,
                                     user=user)
        else:
            if not check.is_active:
                check.is_active = True
                check.save()
            else:
                check.is_active = False
                check.save()
    return redirect(request.META['HTTP_REFERER'])
