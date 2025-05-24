from rest_framework import serializers
from .models import ChatSession, ChatMessage, Profile


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ["id", "role", "content", "created_at"]


class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["image"]


class ChatSessionSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = ["id", "title", "started_at", "messages"]
