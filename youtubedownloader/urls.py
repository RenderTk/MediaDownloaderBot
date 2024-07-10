from django.urls import path
from youtubedownloader import views

urlpatterns = [
    path("hello/", views.hello),
    path(
        "download_video/<str:base64_video_url>/",
        views.download_video_at_highest_quality,
    ),
    path(
        "download_audio/<str:base64_video_url>/",
        views.download_audio_of_video_at_highest_quality,
    ),
]
