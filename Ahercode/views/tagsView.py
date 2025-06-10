from rest_framework import generics

from Ahercode.models import Tags
from Ahercode.serializers import TagsSerializer


# Create a new tip
class TagsCreateView(generics.CreateAPIView):
    """
    API view to create a new tag entry.
    """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

# Get all tag
class TagsListView(generics.ListAPIView):
    """
    API view to retrieve a list of tag entries.
    """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

# Get a single tag, update, and delete
class TagsView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a tag entry.
    """
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer