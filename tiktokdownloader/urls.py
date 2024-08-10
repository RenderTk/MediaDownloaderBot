from django.urls import path
from tiktokdownloader import views

urlpatterns = [
    path("hello/", views.hello),
    path(
        "download_video/",
        views.download_video_at_highest_quality,
    ),
]
