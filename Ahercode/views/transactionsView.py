from rest_framework import generics

from Ahercode.models import Transactions
from Ahercode.serializers import TransactionsSerializer


# Create a new Transaction
class TransactionsCreateView(generics.CreateAPIView):
    """
    API view to create a new Transaction
    """

    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

# Get all Transactions
class TransactionsListView(generics.ListAPIView):
    """
    API view to retrieve a list of Transactions
    """
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

# Get a single Transaction, update, and delete
class TransactionsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete Transaction
    """

    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

