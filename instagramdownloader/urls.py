from django.urls import path
from instagramdownloader import views

urlpatterns = [path("hello/", views.hello)]
