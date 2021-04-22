from django.shortcuts import render
from .models import Profile
from .forms import LoginForm , RegisterForm , UpdateProfile
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.models import User
# Create your views here.


def signin(request):
    if request.method == "POST":
        forms = LoginForm(request.POST)
        if forms is not None:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request , username=username  , password=password)
            if user is not None:
                login (request , user)
                return HttpResponseRedirect(reverse('home:index'))
    else :
        forms = LoginForm()
    return render(request , 'accounts/login.html' , {"forms":forms})



def register(request):
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect(reverse('login:signin'))
    else :
        forms = RegisterForm()
    return render(request , 'accounts/signup.html' , {'forms':forms})


def profile_page(request):
    profile_page = Profile
    return render(request , 'accounts/profile.html' , {"profile":profile_page})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))



def update_profile(request):
    update = UpdateProfile(instance=request.user)
    if request.method == 'POST':
        update = UpdateProfile(request.POST , instance=request.user)
        if update.is_valid():
            update.save()
            return HttpResponseRedirect(reverse('login:profile'))
    else :
        update = UpdateProfile(instance=request.user)
    return render(request , 'accounts/update.html' , {
        'update':update
    })