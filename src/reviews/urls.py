from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CreateTicketView, CreateReviewView, ticket, tickets


urlpatterns = [
    path('list/', tickets, name='tickets'),
    path('<int:id>/', ticket, name='ticket'),
    path('create-ticket/', login_required(CreateTicketView.as_view()), name='create-ticket'),
    path('<int:ticket_id>/create-review/', login_required(CreateReviewView.as_view()), name='create-review'),
]
