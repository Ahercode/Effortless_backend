from rest_framework import generics

from Ahercode.models import Assets
from Ahercode.serializers import AssetsSerializer


# Create a new JournalDetail
class AssetsCreateView(generics.CreateAPIView):
    """
    API view to create a new journalDetail entry.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

# Get all JournalDetails
class AssetsListView(generics.ListAPIView):
    """
    API view to retrieve a list of journalDetail entries.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

# Get a single JournalDetail, update, and delete
class AssetsView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a journalDetail entry.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer