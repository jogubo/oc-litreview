from django.shortcuts import render
from reviews import models


def index(request):
    return render(request, 'index.html')


def ticket(request, id):
    book = models.Ticket.objects.get(id=id)

    return render(
        request,
        'ticket.html',
        {'book': book}
    )
