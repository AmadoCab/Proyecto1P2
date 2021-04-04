from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (
    UserRegisterForm,
    ProfileRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form1 = UserRegisterForm(request.POST)
        form2 = ProfileRegisterForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            person = User.objects.filter(username=username).first()
            person.profile.carrera = form2.cleaned_data.get('carrera')
            person.profile.gender = form2.cleaned_data.get('gender')
            person.profile.save()
            messages.success(request, f'Your account has been crated!')
            return redirect('login')
    else:
        form1 = UserRegisterForm()
        form2 = ProfileRegisterForm()
    return render(request, 'users/register.html', {'form1': form1, 'form2': form2})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)
