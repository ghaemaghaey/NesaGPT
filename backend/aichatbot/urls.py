from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat.as_view(), name="chat"),
    path("chats/", views.chats.as_view(), name="chats"),
]
