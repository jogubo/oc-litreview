from django.urls import path
from .views import LoginPageView, SignupPageView, logout_user


urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', SignupPageView.as_view(), name='signup'),
]
