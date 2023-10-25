from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("user/", views.UserView.as_view()),
]