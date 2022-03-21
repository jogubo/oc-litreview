from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import reviews.forms
import reviews.models
import authentication.forms


def index(request):
    return render(request, 'index.html')


def login_page(request):
    form = authentication.forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = authentication.forms.LoginForm(request.POST)
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
        'login.html',
        {'form': form, 'message': message}
    )


def tickets(request):
    books = reviews.models.Ticket.objects.all()

    return render(
        request,
        'tickets.html',
        {'books': books}
    )


def ticket(request, id):
    book = reviews.models.Ticket.objects.get(id=id)

    return render(
        request,
        'ticket.html',
        {'book': book}
    )


@login_required
def new_ticket(request):
    if request.method == 'POST':
        form = reviews.forms.TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket', ticket.id)

    else:
        form = reviews.forms.TicketForm()

    return render(
        request,
        'new-ticket.html',
        {'form': form}
    )
