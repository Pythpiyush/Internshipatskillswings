from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import UserRegistrationForm
from .models import Profile, User


@login_required
def profile(request):
    return render(request, 'profile/profile.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.phone_no = form.cleaned_data.get('phone_no')
            user.profile.institute = form.cleaned_data.get('institute')
            user.save()

            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=email, password=password)

            login(request, user)
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
