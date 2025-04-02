from rest_framework import generics

from Ahercode.models import AccountDetails
from Ahercode.serializers import AccountDetailsSerializer


# Create a new Account
class AccountDetailCreateView(generics.CreateAPIView):
    """
    API view to create new Account
    """
    queryset = AccountDetails.objects.all()
    serializer_class = AccountDetailsSerializer

# Get all Accounts
class AccountDetailListView(generics.ListAPIView):
    """
    API view retrieve a list of Accounts
    """

    queryset = AccountDetails.objects.all()
    serializer_class = AccountDetailsSerializer

# Get a single Account, update, and delete
class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete an Account
    """

    queryset = AccountDetails.objects.all()
    serializer_class = AccountDetailsSerializer