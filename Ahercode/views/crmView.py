from rest_framework import generics
from Ahercode.models import CRM
from Ahercode.serializers import CRMSerializer

# Create a new CRM
class CRMCreateView(generics.CreateAPIView):
    """
    API view to create new CRM
    """
    queryset = CRM.objects.all()
    serializer_class = CRMSerializer

# Get all CRMs
class CRMListView(generics.ListAPIView):
    """
    API view retrieve a list of CRMs
    """

    queryset = CRM.objects.all()
    serializer_class = CRMSerializer

# Get a single CRM, update, and delete
class CRMView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete an CRM
    """

    queryset = CRM.objects.all()
    serializer_class = CRMSerializer