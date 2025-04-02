from rest_framework import generics

from Ahercode.models import JournalHeaders
from Ahercode.serializers import JournalSerializer


# Create a new Journal header
class JournalHeaderCreateView(generics.CreateAPIView):
    """
    API view to create a new journal.
    """
    queryset = JournalHeaders.objects.all()
    serializer_class = JournalSerializer

# Get all Journal headers
class JournalHeaderListView(generics.ListAPIView):
    """
    API view to retrieve a list of journals.
    """
    queryset = JournalHeaders.objects.all()
    serializer_class = JournalSerializer

# Get a single Journal header, update, and delete
class JournalHeaderView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a journal.
    """
    queryset = JournalHeaders.objects.all()
    serializer_class = JournalSerializer
