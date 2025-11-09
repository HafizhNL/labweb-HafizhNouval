from django.shortcuts import render
from rest_framework import generics, permissions, exceptions
from .serializer import RegisterSerializer, CustomTokenObtainPairSerializer, EvaluationSerializer
from .models import Evaluation
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from rest_framework import serializers

# Minimal user serializer for listing users in the frontend
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'full_name')

# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class EvaluationView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = getattr(self.request, 'user', None)
        if user and getattr(user, 'is_authenticated', False) and isinstance(user, User):
            serializer.save(user=user)
            return

        serializer.save()


class EvaluationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


class UserListView(generics.ListAPIView):
    """Return a lightweight list of users (id, email, username, full_name).

    Requires authentication. Intended for populating selects in the frontend.
    """
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserListSerializer

