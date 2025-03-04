from rest_framework import generics

from Ahercode.models import Journal
from Ahercode.serializers import JournalSerializer


# Create a new Journal
class JournalCreateView(generics.CreateAPIView):
    """
    API view to create a new journal.
    """
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

# Get all Journals
class JournalListView(generics.ListAPIView):
    """
    API view to retrieve a list of journals.
    """
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

# Get a single Journal, update, and delete
class JournalDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a journal.
    """
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
