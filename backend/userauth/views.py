from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from aichatbot import serializers
from . import models
from aichatbot.models import Profile, Balance


class whoami(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # def post(self, request):
    #     this_user = request.user
    #     wallet_update = request.POST.get("amount")
    #     this_text = request.POST.get("text")
    #     this_balance = models.Balance.objects.get(user=this_user)
    #     this_balance.wallet = wallet_update
    #     this_balance.save()
    #     return Response({"wallet": this_balance.wallet})

    def get(self, request):
        this_user = request.user
        session = Profile.objects.get(user=this_user)
        serilizer = serializers.ProfileSerilizer(session)
        this_balance = Balance.objects.get(user=this_user)
        data = {
            "username": this_user.username,
            "email": this_user.email,
            "image": serilizer.data,
            "balance": this_balance.wallet,
        }
        return Response(data=data)
