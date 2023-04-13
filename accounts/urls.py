from django.urls import path

from accounts.views import RegisterView, LoginView, logout_view, ProfileView, UserChangeView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("account/<int:pk>/", ProfileView.as_view(), name="account"),
    path("update/<int:pk>/", UserChangeView.as_view(), name="user_update")
]
