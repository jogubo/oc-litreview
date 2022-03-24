from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,  authenticate
from .forms import LoginForm, SignupForm


def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                message = 'Identifiants incorrects.'

    return render(
        request,
        'authentication/login.html',
        {'form': form, 'message': message}
    )


def logout_user(request):
    logout(request)
    return redirect('logout')


def signup_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    return render(
        request,
        'authentication/signup.html',
        {'form': form}
    )
