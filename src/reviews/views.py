from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Ticket
from .forms import TicketForm
from subscriptions.models import UserFollows


class FluxPageView(View):
    template_name = 'index.html'

    def get(self, request):
        current_user = request.user
        subscribers = []
        for user in UserFollows.objects.all():
            if user.followed_user == current_user:
                subscribers.append(user.user.id)
        return render(
            request,
            self.template_name,
            {'subscribers': subscribers}
        )


class CreateTicketView(View):
    template_name = 'reviews/new-ticket.html',
    form_class = TicketForm

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {'form': form}
        )

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket', ticket.id)
        return render(
            request,
            self.template_name,
            {'form': form}
        )


def tickets(request):
    tickets = Ticket.objects.all()

    return render(
        request,
        'reviews/tickets.html',
        {'tickets': tickets}
    )


def ticket(request, id):
    ticket = Ticket.objects.get(id=id)

    return render(
        request,
        'reviews/ticket.html',
        {'ticket': ticket}
    )
