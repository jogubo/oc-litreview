from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from .models import UserFollows
from .forms import SubscriptionsForm


class SubscriptionsPageView(View):
    template_name = 'subscriptions/subscriptions.html'
    form_class = SubscriptionsForm

    def get(self, request):
        form = self.form_class()
        current_user = request.user
        subscriptions, subscribers = [], []
        for user in UserFollows.objects.all():
            if user.user == current_user:
                subscriptions.append(user.followed_user)
            if user.followed_user == current_user:
                subscribers.append(user.user)

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
