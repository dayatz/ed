from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth


def home(request):
    if request.user.is_authenticated():
        return HttpResponse('home')
    return render(request, 'login.html', locals())


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        auth_check = auth.authenticate(username=username, password=password)
        auth.login(request, auth_check)
        return HttpResponseRedirect("/")
    except Exception, err:
        print err


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')