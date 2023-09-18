from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("home", views.home, name="home"),
    path("ammend", views.ammend, name="ammend"),
    path("info", views.info, name="info"),
]
