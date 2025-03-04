from django.shortcuts import render
from rest_framework import generics

from Ahercode.models import User
from Ahercode.serializers import UserSerializer


# Create a new user
class UserCreateView(generics.CreateAPIView):
    """
    API view to create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Get all users
class UserListView(generics.ListAPIView):
    """
    API view to retrieve a list of users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Get a single user, update, and delete
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer