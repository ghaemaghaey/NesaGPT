from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .pricecheck import pricecheckforapi
from . import models

from rest_framework import viewsets, permissions
from .models import ChatSession
from .serializers import ChatSessionSerializer


# Create your views here.
class chat(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = {"sessions": []}
        outputprice = 0
        this_prompt = request.POST.get("prompt")
        this_user = request.user
        input_price = pricecheckforapi(this_prompt, 4)
        input_price = round(input_price)
        this_balance = models.Balance.objects.get(user=this_user)
        this_balance.wallet = this_balance.wallet - input_price - outputprice
        this_balance.save()
        sessions = models.ChatSession.objects.filter(user=this_user)
        for session in sessions:
            data["sessions"].append(session.title)
        data.update({"wallet": this_balance.wallet})
        return Response(data)


class chats(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        sessions = ChatSession.objects.filter(user=request.user).order_by("-started_at")
        serializer = ChatSessionSerializer(sessions, many=True)
        return Response(serializer.data)
