from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from core.models import (
    UserDetail
)

@login_required(login_url='/server/login')
def server_index(request):
    mylist = {
        "User": "Almas",
        "UID": "001"
    }
    return JsonResponse(mylist, safe=False)


def login(request):
    if request.user.is_anonymous == False:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            username = User.objects.get(email=email.lower()).username
            user = authenticate(username=username, password=password)
        except:
            return HttpResponse(request, '404')
        if user is not None:
            userDtl = request.META.get('HTTP_USER_AGENT')
            UserDetail(user=username, value=userDtl).save()
            login(request, user)
            return redirect('/server')
        else:
            return HttpResponse(request, '404')


def logoutUser(request):
    logout(request)
    return redirect('/server')
