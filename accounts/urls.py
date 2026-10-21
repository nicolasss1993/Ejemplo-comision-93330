from django.contrib.auth import views
from django.urls import path

from accounts.views import *

urlpatterns = [
    path("registro/", registro, name="registro"),
    path("login/", views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("perfil/", perfil, name="perfil"),
    path("perfil/editar", editar_perfil, name="editar_perfil"),
    path(
        "password/cambiar",
        views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html", success_url="/accounts/password/cambiada"
        ),
        name="password_change",
    ),
    path(
        "password/cambiada",
        views.PasswordChangeDoneView.as_view(template_name="accounts/passsword_change_done.html"),
        name="password_change_done",
    ),
]
