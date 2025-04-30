
from rest_framework import generics
from django.core.mail import send_mail
from Ahercode.models import Subscribers
from Ahercode.serializers import SubscriberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from Ahercode.models import Subscribers


# Create a new Subscriber
class SubscriberCreateView(generics.CreateAPIView):
    """
    API view to create a new Subscriber.
    """
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer
    
    def perform_create(self, serializer):
        # Get the raw password from the validated data
        temp_password = serializer.validated_data.get('password')

        # Hash the password before saving
        hashed_password = make_password(temp_password)

        # Save the subscriber with the hashed password
        subscriber = serializer.save(password=hashed_password)

        # Send registration email
        send_mail(
            subject="Registration Successful",
            message=f"Dear {subscriber.first_name},\n\nThank you for registering. " +
            f"\nFind below your temporary login details:" +
            f"\nUsername: {subscriber.email}" + 
            f"\nPassword: {temp_password}" +
            "\n\nWe will review your details for approval.\n\nBest regards,\nSIP Consult Team",
            from_email="sipconsult.net@gmail.com",
            recipient_list=[subscriber.email],
        )

# Get all Subscribers
class SubscriberListView(generics.ListAPIView):
    """
    API view to retrieve a list of Subscribers.
    """
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer

# Get a single Subscriber, update, and delete
class SubscriberDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a Subscriber.
    """
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer
    
    
class SubscriberApprovalView(APIView):
    
    def post(self, request, subscriber_id):
        subscriber = Subscribers.objects.get(id=subscriber_id)
        subscriber.status = "approved"
        subscriber.save()
        # Send approval email
        send_mail(
            subject="Account Approved",
            message=f"Dear {subscriber.first_name},\n\nYour account has been approved. You can now log in.",
            from_email="no-reply@example.com",
            recipient_list=[subscriber.email],
        )
        return Response({"message": "Subscriber approved and email sent."})
    
