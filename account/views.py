from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, UserRegistrationForm


def register_view(request):
    """Register a new user."""
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new User object but don't save it yet.
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data["password"]
            )
            # Save the User object
            new_user.save()

            context = {"user_form": user_form}

            return render(request, "account/register_done.html", context)

    else:
        user_form = UserRegistrationForm()

    return render(request, "account/register.html", {"user_form": user_form})


def user_login_view(request):
    """Log in a user."""

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd["username"],
                                password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return HttpResponse("Authenticated successfully")

                else:
                    return HttpResponse("Disabled account")

            else:
                return HttpResponse("Invalid login")

    else:
        form = LoginForm()

    context = {
        "form": form
    }
    return render(request, "account/login.html", context)


@login_required
def dashboard_view(request):
    context = {
        "section": "dashboard"
    }
    return render(request, "account/dashboard.html", context)
