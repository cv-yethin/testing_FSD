from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import SignupForm

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created. You are now logged in.")
            login(request, user)
            return redirect("accounts:dashboard")
        messages.error(request, "Please correct the errors below.")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})

class SignInView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

class SignOutView(LogoutView):
    next_page = reverse_lazy("accounts:login")

@login_required
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")