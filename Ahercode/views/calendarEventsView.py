from rest_framework import generics

from Ahercode.models import CalendarEvents
from Ahercode.serializers import CalendarEventsSerializer


# Create a new Account
class CalendarEventCreateView(generics.CreateAPIView):
    """
    API view to create new Account
    """
    queryset = CalendarEvents.objects.all()
    serializer_class = CalendarEventsSerializer

# Get all Accounts
class CalendarEventListView(generics.ListAPIView):
    """
    API view retrieve a list of Accounts
    """

    queryset = CalendarEvents.objects.all()
    serializer_class = CalendarEventsSerializer

# Get a single Account, update, and delete
class CalendarEventView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete an Account
    """

    queryset = CalendarEvents.objects.all()
    serializer_class = CalendarEventsSerializer