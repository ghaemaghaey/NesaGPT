from django.conf import settings

from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from openai import OpenAI

from .models import ChatSession, ChatMessage, Balance
from .serializers import ChatSessionSerializer, UserSerializer
from .service import pricecheckforapi


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
        this_balance = Balance.objects.get(user=this_user)
        this_balance.wallet = this_balance.wallet - input_price - outputprice
        this_balance.save()
        sessions = ChatSession.objects.filter(user=this_user)
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

    def post(self, request):
        this_user = request.user
        content = request.data.get("content")
        sessinid = int(request.data.get("sessionid"))
        session = ChatSession.objects.get(id=sessinid)
        ChatMessage.objects.create(role="user", session=session, content=content)
        try:
            clinet = OpenAI(api_key=settings.OPENAI_API_KEY)
            userbalance = Balance.objects.get(user=this_user)
            userbalance.wallet - openaiResponse.usage.total_tokens
            openaiResponse = clinet.responses.create(model="gpt-4-turbo", input=content)
            ChatMessage.objects.create(
                role="assistant", session=session, content=openaiResponse.output_text
            )
            userbalance.save()
        except:
            return Response({"result": "failure"})
        # here we write the api connection data
        return Response({"result": "sucess"})


class newChatSession(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        this_user = request.user
        this_title = request.data.get("title")
        session = ChatSession.objects.create(user=this_user, title=this_title)
        return Response({"result": "ok", "sessionid": session.id})


class signup(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
