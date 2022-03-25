from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CreateTicketView, ticket, tickets


urlpatterns = [
    path('list/', tickets, name='tickets'),
    path('<int:id>/', ticket, name='ticket'),
    path('create-ticket/', login_required(CreateTicketView.as_view()), name='create-ticket'),
]
