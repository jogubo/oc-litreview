from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Ticket, Review
from .forms import TicketForm, ReviewForm
from subscriptions.models import UserFollows


class FluxPageView(View):
    template_name = 'index.html'

    def get(self, request):
        subscribers = []
        for user in UserFollows.objects.all():
            if user.followed_user == request.user:
                subscribers.append(user.user)
        tickets = Ticket.objects.filter(user__in=subscribers)
        return render(
            request,
            self.template_name,
            {'tickets': tickets}
        )


class PostPageView(View):
    template_name = 'reviews/posts.html'

    def get(self, request):
        # posts = []
        tickets = Ticket.objects.filter(user=request.user).order_by('-time_created')
        # reviews = Review.objects.filter(user=request.user)
        return render(
            request,
            self.template_name,
            {'tickets': tickets}
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


class CreateReviewView(View):
    template_name = 'reviews/create-review.html',
    form_class = ReviewForm

    def get(self, request, ticket_id=None):
        form = self.form_class()
        ticket = Ticket.objects.get(id=ticket_id)
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'ticket': ticket,
            }
        )

    def post(self, request, ticket_id=None):
        form = self.form_class(request.POST, request.FILES)
        ticket = Ticket.objects.get(id=ticket_id)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('index')
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
