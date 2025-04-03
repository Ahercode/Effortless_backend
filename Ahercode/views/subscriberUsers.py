from django.shortcuts import render
from rest_framework import generics

from Ahercode.models import SubscriberUsers
from Ahercode.serializers import SubscriberUserSerializer


# Create a new user
class SubscriberUserCreateView(generics.CreateAPIView):
    """
    API view to create a new user.
    """
    queryset = SubscriberUsers.objects.all()
    serializer_class = SubscriberUserSerializer

# Get all users
class SubscriberUserListView(generics.ListAPIView):
    """
    API view to retrieve a list of users.
    """
    queryset = SubscriberUsers.objects.all()
    serializer_class = SubscriberUserSerializer

# Get a single user, update, and delete
class SubscriberUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a user.
    """
    queryset = SubscriberUsers.objects.all()
    serializer_class = SubscriberUserSerializer