from django.urls import path

from accounts.views import RegisterView, logout_view

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", logout_view, name="logout"),
]
