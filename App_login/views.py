from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_login.forms import SignUpForm
# Create your views here.

def signup(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm( data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form, 'registered':registered}
    return render(request, 'App_login/signup.html', context=dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=Username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_login/login.html', context={'form':form})
@login_required                
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))