from django.urls import path , include
from .views import TokenObtainPairView, RegisterView
from .views import ChatMessageListCreate

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='registertion'),
    path('chat/', ChatMessageListCreate.as_view(), name='chat'),

]






