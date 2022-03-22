from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import LoginForm


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
                message = f'Bonjour {user.username}.'
            else:
                message = 'Identifiants incorrects.'

    return render(
        request,
        'authentication/login.html',
        {'form': form, 'message': message}
    )
