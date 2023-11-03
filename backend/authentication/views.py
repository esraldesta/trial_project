from django.shortcuts import render
from django.contrib.auth.models import User
from  rest_framework.generics import CreateAPIView
from .serializers import SignupSerializer
# Create your views here.

class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

