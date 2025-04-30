from rest_framework import serializers
from .models import User, JournalHeaders, Subscribers, SubscriberUsers, Account, AccountDetails, Party, Journals, \
    Transactions, InExDetails, CalendarEvents, Assets



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password
from Ahercode.models import Subscribers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    username_field = 'email'  # Use email as the username field
    
    def validate(self, attrs):
        email = attrs.get(self.username_field)  # `username` is used by default for JWT
        password = attrs.get("password")

        # Check if the subscriber exists
        subscriber = Subscribers.objects.filter(email=email).first()
        if not subscriber:
            raise AuthenticationFailed("Subscriber with this email does not exist.")

        # Check if the account is approved
        if subscriber.status != "approved":
            raise AuthenticationFailed("Your account is not approved yet.")

        # Validate the password
        if not check_password(password, subscriber.password):
            raise AuthenticationFailed("Invalid password.")

        # Generate tokens
        refresh = self.get_token(subscriber)
        data = {
            "refresh": str(refresh),
            "jwt_token": str(refresh.access_token),
        }
        
        data["email"] = subscriber.email
        data["first_name"] = subscriber.first_name
        data["last_name"] = subscriber.last_name
        data["id"] = subscriber.id
        
        return data
    
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

class CalendarEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvents
        fields = '__all__'

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'