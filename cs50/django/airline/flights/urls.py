from django.urls import path, include
from . import views

app_name = "flights"

urlpatterns = [
    path("", views.index, name="index"),
]
