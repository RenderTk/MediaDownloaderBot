from django.urls import path
from instagramdownloader import views

urlpatterns = [
    path("hello/", views.hello),
    path(
        "download_video/",
        views.download_video_at_highest_quality,
    ),
]
