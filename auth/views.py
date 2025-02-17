from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(APIView):
   permission_classes=[AllowAny]
   def get(self, request):
      return Response({"message":
 "Register endpoint is working!"},
status=status.HTTP_200_OK)
   def post(self, request):
      return Response({"message":
 "user registered successfully"},
status=status.HTTP_201_CREATED)
   
