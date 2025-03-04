
from rest_framework import generics

from Ahercode.models import Subscriber
from Ahercode.serializers import SubscriberSerializer


# Create a new Subscriber
class SubscriberCreateView(generics.CreateAPIView):
    """
    API view to create a new Subscriber.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

# Get all Subscribers
class SubscriberListView(generics.ListAPIView):
    """
    API view to retrieve a list of Subscribers.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

# Get a single Subscriber, update, and delete
class SubscriberDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a Subscriber.
    """
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer