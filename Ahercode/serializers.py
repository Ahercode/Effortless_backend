from rest_framework import serializers
from .models import User, JournalHeaders, Subscribers, SubscriberUsers, Account, AccountDetails, Party, Journals, Transactions, InExDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'

class SubscriberUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriberUsers
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountDetails
        fields = '__all__'

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalHeaders
        fields = '__all__'

class JournalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journals
        fields = '__all__'

class InExDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InExDetails
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'