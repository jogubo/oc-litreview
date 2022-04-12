from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import SubscriptionsPage, DeleteSubscription


urlpatterns = [
    path(
        '',
        login_required(SubscriptionsPage.as_view()),
        name='subscriptions'
    ),
    path(
        '<int:sub_id>/delete',
        login_required(DeleteSubscription.as_view()),
        name='delete_subscription'
    ),
]
