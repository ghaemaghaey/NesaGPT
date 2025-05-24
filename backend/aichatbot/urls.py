from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat.as_view(), name="chat"),
    path('chat/',views.sendchat.as_view()),
    path("session/create/",views.newChatSession.as_view(),name="createsession"),
    path("chats/", views.chats.as_view(), name="chats"),
]
