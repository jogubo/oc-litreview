from django.urls import path
from .views import ticket, tickets, new_ticket


urlpatterns = [
    path('list/', tickets, name='tickets'),
    path('<int:id>/', ticket, name='ticket'),
    path('new/', new_ticket, name='new-ticket'),
]
