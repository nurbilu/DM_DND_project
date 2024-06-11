from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, ChatMessageSerializer
import os
import google.generativeai as genai
from django.http import JsonResponse
from rest_framework.views import APIView

# Configure the Google AI Python SDK with the environment variable
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user, context=self.get_serializer_context()).data
        }, status=status.HTTP_201_CREATED)

class ChatView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatMessageSerializer

    def post(self, request, *args, **kwargs):
        user_input = request.data.get('message')
        
        # Create the model with a detailed configuration
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 150,
            "response_mime_type": "text/plain",
        }
        
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=generation_config
        )

        # Start a chat session with the model
        chat_session = model.start_chat(history=[])
        
        # Send a message to the model and get the response
        response = chat_session.send_message(user_input)
        
        # Return the response text
        return JsonResponse({'response': response.text})
