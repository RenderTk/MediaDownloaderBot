from django.urls import path
from youtubedownloader import views

urlpatterns = [path("hello/", views.hello)]
