from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .pricecheck import pricecheckforapi
from . import models
from django.conf import settings
from django.shortcuts import HttpResponse
from requests import get,post
from openai import OpenAI
from rest_framework import viewsets, permissions
from .models import ChatSession,ChatMessage
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


class sendchat(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        this_user = request.user
        content = request.data.get("content")
        sessinid = int(request.data.get('sessionid'))
        session = ChatSession.objects.get(id=sessinid)
        print(content)
        ChatMessage.objects.create(role="user",session = session,content=content)
        clinet = OpenAI(api_key=settings.OPENAI_API_KEY)
        print(settings.OPENAI_API_KEY)
        openaiResponse = clinet.responses.create(
            model='gpt-4-turbo',
            input=content
        )
        ChatMessage.objects.create(role="assistant",session=session,content=openaiResponse.output_text)
        # here we write the api connection data
        return Response({"result":"sucess"})


class newChatSession(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        this_user = request.user
        this_title = request.data.get("title")
        session = ChatSession.objects.create(user=this_user, title=this_title)
        return Response({"result": "ok", "sessionid": session.id})
