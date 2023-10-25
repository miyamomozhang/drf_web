from django.urls import path
from . import views

urlpatterns = [
    # FBV
    path("auth/", views.auth),
    path("login/", views.login),
    # CBV
    path("user/", views.UserView.as_view()),
    path("info/", views.InfoView.as_view()),
]
