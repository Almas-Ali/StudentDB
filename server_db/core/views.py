from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from core.models import (
    UserDetail
)


@login_required(login_url='/server/login')
def server_index(request):
    user = User.objects.get(username=request.user.username)
    mylist = {
        "User": user.username,
        "UID": user.id
    }
    return JsonResponse(mylist, safe=False)


def get_ip(request):
    '''User IP catcher.'''
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        ip = forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@csrf_exempt
def loginX(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            u = User.objects.get(email=email.lower())
            user = authenticate(username=u.username, password=password)
        except:
            return HttpResponse('404')
        else:
            if user is not None:
                userDtl = f"{request.META.get('HTTP_USER_AGENT')} ## ip: {get_ip(request)}"
                UserDetail(user=u, value=userDtl).save()
                login(request, user)
                return redirect('/server')
            else:
                return render(request, 'login.html')
    if request.user.is_anonymous == False:
        return HttpResponse('404')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('/')


def index(request):
    return HttpResponse('404')
