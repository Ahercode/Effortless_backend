from rest_framework import generics

from Ahercode.models import InExDetails
from Ahercode.serializers import InExDetailsSerializer


# Create a new inExDetail
class InExDetailsCreateView(generics.CreateAPIView):
    """
    API view to create a new inExDetail entry.
    """
    queryset = InExDetails.objects.all()
    serializer_class = InExDetailsSerializer

# Get all JournalDetails
class InExDetailsListView(generics.ListAPIView):
    """
    API view to retrieve a list of inExDetail entries.
    """
    queryset = InExDetails.objects.all()
    serializer_class = InExDetailsSerializer

# Get a single JournalDetail, update, and delete
class InExDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a inExDetail entry.
    """
    queryset = InExDetails.objects.all()
    serializer_class = InExDetailsSerializer