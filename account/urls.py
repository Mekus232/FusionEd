from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginUsers, name="login"),
    path("logout/", views.loginUsers, name="logout")
]