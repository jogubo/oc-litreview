from django.urls import path
from .views import login_page, logout_user, signup_page


urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_page, name='signup'),
]
