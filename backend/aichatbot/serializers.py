from rest_framework import serializers
from .models import ChatSession, ChatMessage, Profile
import jdatetime


class ChatMessageSerializer(serializers.ModelSerializer):
    jalali_created_at = serializers.SerializerMethodField()

    class Meta:
        model = ChatMessage
        fields = ['id', 'role', 'content', 'jalali_created_at']

    def get_jalali_created_at(self, obj):
        return jdatetime.datetime.fromgregorian(datetime=obj.created_at).strftime('%Y/%m/%d - %H:%M')
class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["image"]


class ChatSessionSerializer(serializers.ModelSerializer):
    messages = ChatMessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = ["id", "title", "started_at", "messages"]
