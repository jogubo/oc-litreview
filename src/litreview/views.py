from django.shortcuts import render, redirect
from reviews import models, forms


def index(request):
    return render(request, 'index.html')


def tickets(request):
    books = models.Ticket.objects.all()

    return render(
        request,
        'tickets.html',
        {'books': books}
    )


def ticket(request, id):
    book = models.Ticket.objects.get(id=id)

    return render(
        request,
        'ticket.html',
        {'book': book}
    )


def new_ticket(request):
    if request.method == 'POST':
        form = forms.TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('ticket', ticket.id)

    else:
        form = forms.TicketForm()

    return render(
        request,
        'new-ticket.html',
        {'form': form}
    )
