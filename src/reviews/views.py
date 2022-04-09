from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Value, CharField
from .models import Ticket, Review
from .forms import TicketForm, ReviewForm
from subscriptions.models import UserFollows
from itertools import chain


class FluxPage(View):
    template_name = 'index.html'

    def get(self, request):
        subscribers = []
        for user in UserFollows.objects.all():
            if user.followed_user == request.user:
                subscribers.append(user.user)

        tickets = (
            Ticket.objects.filter(user=request.user) |
            Ticket.objects.filter(user__in=subscribers)
        )
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

        reviews = (
            Review.objects.filter(user=request.user) |
            Review.objects.filter(user__in=subscribers)
        )
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

        posts = chain(tickets, reviews)
        posts = sorted(posts, key=lambda post: post.time_created, reverse=True)

        return render(
            request,
            self.template_name,
            {'posts': posts}
        )


class PostPage(View):
    template_name = 'reviews/posts.html'

    def get(self, request):
        tickets = Ticket.objects.filter(user=request.user)
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

        reviews = Review.objects.filter(user=request.user)
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

        posts = chain(tickets, reviews)
        posts = sorted(posts, key=lambda post: post.time_created, reverse=True)

        return render(
            request,
            self.template_name,
            {'posts': posts}
        )


class CreateTicket(View):
    template_name = 'reviews/ticket_form.html',
    form_class = TicketForm

    def get(self, request):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'mode': 'CREATION'
            }
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
            {
                'form': form,
                'mode': 'CREATION'
            }
        )


class UpdateTicket(View):
    form_class = TicketForm
    template_name = 'reviews/ticket_form.html',

    def get(self, request, ticket_id=None):
        ticket = Ticket.objects.get(id=ticket_id)
        form = self.form_class(instance=ticket)
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'mode': 'EDITING'
            }
        )

    def post(self, request, ticket_id=None):
        ticket = Ticket.objects.get(id=ticket_id)
        form = self.form_class(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            ticket.resize_image()
            return redirect('posts')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'mode': 'EDITING'
            }
        )


class CreateReview(View):
    template_name = 'reviews/review_form.html',
    ticket_form_class = TicketForm
    review_form_class = ReviewForm

    def get(self, request):
        ticket_form = self.ticket_form_class()
        review_form = self.review_form_class()
        return render(
            request,
            self.template_name,
            {
                'ticket_form': ticket_form,
                'review_form': review_form,
                'existing_ticket': False,
                'mode': 'CREATION'
            }
        )

    def post(self, request, ticket_id=None):
        ticket_form = self.ticket_form_class(request.POST, request.FILES)
        review_form = self.review_form_class(request.POST, request.FILES)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            review.ticket.has_review = True
            review.ticket.save()
            return redirect('index')
        return render(
            request,
            self.template_name,
            {
                'ticket_form': ticket_form,
                'review_form': review_form,
                'existing_ticket': False,
                'mode': 'CREATION'
            }
        )


class CreateReviewExistingTicket(View):
    template_name = 'reviews/review_form.html',
    form_class = ReviewForm

    def get(self, request, ticket_id=None):
        form = self.form_class()
        ticket = Ticket.objects.get(id=ticket_id)
        return render(
            request,
            self.template_name,
            {
                'review_form': form,
                'ticket': ticket,
                'existing_ticket': True,
                'mode': 'CREATION'
            }
        )

    def post(self, request, ticket_id=None):
        form = self.form_class(request.POST, request.FILES)
        ticket = Ticket.objects.get(id=ticket_id)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.ticket.has_review = True
            review.save()
            review.ticket.save()
            return redirect('index')
        return render(
            request,
            self.template_name,
            {
                'review_form': form,
                'ticket': ticket,
                'existing_ticket': True,
                'mode': 'CREATION'
            }
        )


class UpdateReview(View):
    form_class = ReviewForm
    template_name = 'reviews/review_form.html',

    def get(self, request, review_id=None):
        review = Review.objects.get(id=review_id)
        form = self.form_class(instance=review)
        return render(
            request,
            self.template_name,
            {
                'review_form': form,
                'ticket': review.ticket,
                'existing_ticket': True,
                'mode': 'EDITING'
            }
        )

    def post(self, request, review_id=None):
        review = Review.objects.get(id=review_id)
        form = self.form_class(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('posts')
        return render(
            request,
            self.template_name,
            {
                'review_form': form,
                'ticket': review.ticket,
                'existing_ticket': True,
                'mode': 'EDITING'
            }
        )
