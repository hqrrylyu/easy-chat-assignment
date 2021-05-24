from django.urls import path, re_path

from . import consumers, views

app_name = "chat"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]

websocket_urlpatterns = [
    re_path(r"^ws/$", consumers.ChatConsumer.as_asgi()),
]
