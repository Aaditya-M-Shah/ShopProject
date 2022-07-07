from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form =  UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your account has been succesfully created! Login Now")
            return redirect('login')
    else:
        user_form = UserRegisterForm()
    return render(request, 'Users/register.html', {"form": user_form})
        
@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your account has been successfully updated!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance= request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form":user_form, "p_form":profile_form}
    return render(request, 'Users/profile.html', context)