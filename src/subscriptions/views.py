from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from .models import UserFollows
from .forms import SubscriptionsForm


class SubscriptionsPage(View):
    template_name = 'subscriptions/subscriptions.html'
    form_class = SubscriptionsForm

    def get(self, request):
        form = self.form_class()
        current_user = request.user
        subscriptions, subscribers = [], []
        for sub in UserFollows.objects.all():
            if sub.user == current_user:
                subscriptions.append(sub)
            if sub.followed_user == current_user:
                subscribers.append(sub.user)

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'current_user': current_user,
                'subscriptions': subscriptions,
                'subscribers': subscribers
            }
        )

    def post(self, request):
        form = self.form_class(request.POST)
        users = User.objects.all()
        if form.is_valid():
            entry = request.POST['username']
            user_to_follow = User.objects.get(username=entry)
            for user in users:
                if user.username == entry:
                    UserFollows.objects.create(
                        user=request.user,
                        followed_user=user_to_follow
                    )
            return redirect('subscriptions')

        return render(
            request,
            self.template_name,
            {'form': form}
        )


class DeleteSubscription(View):
    template_name = 'subscriptions/deletion_form.html',

    def get(self, request, sub_id=None):
        subscription = UserFollows.objects.get(id=sub_id)
        if subscription.user == request.user:
            return render(
                request,
                self.template_name,
                {'followed_user': subscription.followed_user}
            )

    def post(self, request, sub_id=None):
        subscription = UserFollows.objects.get(id=sub_id)
        if subscription.user == request.user:
            subscription.delete()
            return redirect('subscriptions')
