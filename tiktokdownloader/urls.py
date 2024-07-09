from django.urls import path
from tiktokdownloader import views

urlpatterns = [path("hello/", views.hello)]
