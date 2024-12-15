from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_login.forms import SignUpForm, UserProfileChange, ProfilePicForm
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

@login_required
def profile(request):
    return render(request, 'App_login/profile.html', context={})

@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
    return render(request, 'App_login/change_profile.html', context={'form':form})

@login_required
def pass_change(request):
    current_user=request.user
    form=PasswordChangeForm(user=current_user)
    changed=False
    if request.method=='POST':
        form=PasswordChangeForm(user=current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed=True
    return render(request,'App_login/pass_change.html',context={'form':form,'changed':changed})

@login_required

def add_pro_pic(request):
    form = ProfilePicForm()
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_login/pro_pic_add.html', context={'form':form})

@login_required

def change_pro_pic(request):
    form = ProfilePicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_login/pro_pic_add.html', context={'form':form})