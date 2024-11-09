from django.urls import path
from .views import signup_view, login_view, logout_view, profile_view

urlpatterns = [
    path('users/signup/', signup_view),
    path('users/login/', login_view),
    path('users/logout/', logout_view ),
    path('users/profile/', profile_view),
]