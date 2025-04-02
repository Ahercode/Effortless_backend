from rest_framework import generics

from Ahercode.models import Account
from Ahercode.serializers import AccountSerializer


# Create a new Account
class AccountCreateView(generics.CreateAPIView):
    """
    API view to create new Account
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Get all Accounts
class AccountListView(generics.ListAPIView):
    """
    API view retrieve a list of Accounts
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Get a single Account, update, and delete
class AccountView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete an Account
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer