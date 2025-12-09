from django.urls import path
from .views import signup_view, SignInView, SignOutView, dashboard_view

app_name = "accounts"

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", SignInView.as_view(), name="login"),
    path("logout/", SignOutView.as_view(), name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
]