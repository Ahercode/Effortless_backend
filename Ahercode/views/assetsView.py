from rest_framework import generics

from Ahercode.models import Assets
from Ahercode.serializers import AssetsSerializer


# Create a new asset
class AssetsCreateView(generics.CreateAPIView):
    """
    API view to create a new asset entry.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

# Get all asset
class AssetsListView(generics.ListAPIView):
    """
    API view to retrieve a list of asset entries.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

# Get a single asset, update, and delete
class AssetsView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a asset entry.
    """
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer