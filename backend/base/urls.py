from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ChatView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('api/register/', RegisterView.as_view(), name='api_register'),
    path('api/chat/', ChatView.as_view(), name='chat'),
]







