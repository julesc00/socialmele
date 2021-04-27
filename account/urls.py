from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = "account"

urlpatterns = [
    # path("login/", views.user_login_view, name="login"),
    path("", views.dashboard_view, name="dashboard"),

    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Change password urls
    path("password_change/",
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("account:password_change_done")),
         name="password_change"),
    path("password_change/done/",
         auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
]
