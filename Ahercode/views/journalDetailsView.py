from rest_framework import generics

from Ahercode.models import JournalDetails
from Ahercode.serializers import JournalDetailsSerializer


# Create a new JournalDetail
class JournalDetailsCreateView(generics.CreateAPIView):
    """
    API view to create a new journalDetail entry.
    """
    queryset = JournalDetails.objects.all()
    serializer_class = JournalDetailsSerializer

# Get all JournalDetails
class JournalDetailsListView(generics.ListAPIView):
    """
    API view to retrieve a list of journalDetail entries.
    """
    queryset = JournalDetails.objects.all()
    serializer_class = JournalDetailsSerializer

# Get a single JournalDetail, update, and delete
class JournalDetailsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a journalDetail entry.
    """
    queryset = JournalDetails.objects.all()
    serializer_class = JournalDetailsSerializer