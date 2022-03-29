from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SubscriptionsPageView


urlpatterns = [
    path('', login_required(SubscriptionsPageView.as_view()), name='subscriptions'),
]
