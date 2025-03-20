from . import views
from django.urls import path, include



urlpatterns = [
    path("", views.index, name="index"),
    path("staticview/", views.static_view, name="static_view"),
    path("list/", views.list_view, name="list"),
    path("dynamic/", views.dynamic_view, name="dynamic"),
]
