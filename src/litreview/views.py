from django.shortcuts import render
from reviews import models


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
