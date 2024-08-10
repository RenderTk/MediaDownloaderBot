from django.urls import path
from youtubedownloader import views

urlpatterns = [
    path("hello/", views.hello),
    path(
        "download_video/",
        views.download_video_at_highest_quality,
    ),
    path(
        "download_audio/",
        views.download_audio_of_video_at_highest_quality,
    ),
]
