from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    if request.user.is_authenticated():
        return HttpResponse('home')
    return render(request, 'login.html', locals())