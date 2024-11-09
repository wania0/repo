from django.urls import path

from .views import signup_view, login_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("signup/", signup_view),
    path("login/", login_view, name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]