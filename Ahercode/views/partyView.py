from rest_framework import generics

from Ahercode.models import Party
from Ahercode.serializers import PartySerializer


# Create a new Party
class PartyCreateView(generics.CreateAPIView):
    """
    API view to create a new Party
    """

    queryset = Party.objects.all()
    serializer_class = PartySerializer

# Get all Parties
class PartyListView(generics.ListAPIView):
    """
    API view retrieve a list of Party
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer

# Get a single Party, update, and delete
class PartyDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view retrieve, update, or delete a party
    """

    queryset = Party.objects.all()
    serializer_class = PartySerializer
