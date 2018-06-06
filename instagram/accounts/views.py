from django.shortcuts import render, redirect
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from . import views
from django.contrib.auth.views import login, logout
from . forms import RegistrationForm, EditProfileForm

# Create your views here.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#authentication
def index(request):
    return render(request,'index.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else: 
        form = RegistrationForm()
        return render(request, 'accounts/registration.html', {'form':form })

def login_redirect(request):
    return render(request, 'index.html')

#---------------------------------------------------------------------------------------------------------------------------------------
#profile views
def view_profile(request):
    args = {'user':request.user} 
    return render(request,'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form':form}
        return render(request, 'accounts/edit_profile.html', args)