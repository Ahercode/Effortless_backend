from rest_framework import generics

from Ahercode.models import Tips
from Ahercode.serializers import TipsSerializer


# Create a new tip
class TipsCreateView(generics.CreateAPIView):
    """
    API view to create a new tip entry.
    """
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer

# Get all tip
class TipsListView(generics.ListAPIView):
    """
    API view to retrieve a list of tip entries.
    """
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer

# Get a single tip, update, and delete
class TipsView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a tip entry.
    """
    queryset = Tips.objects.all()
    serializer_class = TipsSerializer