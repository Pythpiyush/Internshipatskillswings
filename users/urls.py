from django.urls import path, include
from allauth.account.views import LoginView, SignupView
from users.views import (
    profile,
    signup,
    logout_view,
)


urlpatterns = [
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('redirect/login/', LoginView.as_view(), name="redirect_login"),
    path('redirect/signup/', SignupView.as_view(), name="redirect_singup"),
]
