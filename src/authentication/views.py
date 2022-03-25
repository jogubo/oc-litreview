from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,  authenticate
from django.views.generic import View
from .forms import LoginForm, SignupForm


class LoginPageView(View):
    template_name = 'authentication/login.html',
    form_class = LoginForm
    message = ''

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(
            request,
            self.template_name,
            {'form': form, 'message': message}
        )

    def post(self, request):
        form = self.form_class(request.POST)
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
            self.template_name,
            {'form': form, 'message': message}
        )


class SignupPageView(View):
    template_name = 'authentication/signup.html',
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {'form': form}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        return render(
            request,
            self.template_name,
            {'form': form}
        )


def logout_user(request):
    logout(request)
    return redirect('login')
