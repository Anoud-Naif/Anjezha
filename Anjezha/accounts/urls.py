from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("profile/<user_id>/", views.user_profile_view, name="user_profile_view"),
    path("register/", views.register_view, name="register_view"),


]