from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views

from . import views

app_name = "account"

urlpatterns = [
    # path("login/", views.user_login_view, name="login"),
    path("", views.dashboard_view, name="dashboard"),
    path("register/", views.register_view, name="register"),

    # Authentication urls
    # path("login/", auth_views.LoginView.as_view(), name="login"),
    # path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Use Django's authentication URLs
    path("", include("django.contrib.auth.urls")),

    # Change password urls
    path("password_change/",
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("account:password_change_done")),
         name="password_change"),
    path("password_change/done/",
         auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),

    # Reset password urls
    path("password_reset/",
         auth_views.PasswordResetView.as_view(
             template_name="registration/password_reset_form.html",
             success_url=reverse_lazy("account:password_reset_done")
         ),
         name="password_reset"),
    path("password_rest/done/",
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(
             template_name="registration/password_reset_confirm.html",
             success_url=reverse_lazy("account:password_reset_complete")
         ),
         name="password_reset_confirm"),
    path("reset/done/",
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
         name="password_reset_complete"),
]
