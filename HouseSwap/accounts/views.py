from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

 # Create your views here.
def register(request):
    user_form = UserForm()
    profile_form=ProfileForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form=ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'There was a problem with your signup data, please try again')
    return render(request, 'registration/register.html', {'user_form': user_form,'profile_form':profile_form})

@login_required
def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=profile)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
       
    return render(request, 'registration/update_profile.html', {'user_form': user_form,'profile_form': profile_form})

     
