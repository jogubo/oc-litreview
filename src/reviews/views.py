from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm


def tickets(request):
    books = Ticket.objects.all()

    return render(
        request,
        'reviews/tickets.html',
        {'books': books}
    )


def ticket(request, id):
    book = Ticket.objects.get(id=id)

    return render(
        request,
        'reviews/ticket.html',
        {'book': book}
    )


@login_required
def new_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket', ticket.id)

    else:
        form = TicketForm()

    return render(
        request,
        'reviews/new-ticket.html',
        {'form': form}
    )
