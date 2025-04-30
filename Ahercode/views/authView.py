from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from Ahercode.models import Subscribers
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import random
import string
from Ahercode.serializers import CustomTokenObtainPairSerializer

class LoginView(TokenObtainPairView):
    """
    Custom login view using JWT authentication.
    """
    
    serializer_class = CustomTokenObtainPairSerializer
    
    

class ChangePasswordView(APIView):
    """
    API view to allow subscribers to change their password.
    """

    def post(self, request):
        # Get the authenticated subscriber
        subscriber = request.user  # Assumes the subscriber is authenticated via JWT
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        # Validate input
        if not old_password or not new_password:
            return Response({"error": "Both old_password and new_password are required."}, status=400)

        # Check if the old password is correct
        if not check_password(old_password, subscriber.password):
            return Response({"error": "Old password is incorrect."}, status=400)

        # Set the new password
        subscriber.password = make_password(new_password)
        subscriber.save()

        return Response({"message": "Password changed successfully."})
    
    
class ResetPasswordView(APIView):
    """
    API view to reset a subscriber's password.
    """

    def post(self, request):
        email = request.data.get("email")
        subscriber = Subscribers.objects.filter(email=email).first()

        if not subscriber:
            return Response({"error": "Subscriber with this email does not exist."}, status=404)

        # Generate a temporary password
        temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        subscriber.password = make_password(temp_password)
        subscriber.save()

        # Send the temporary password via email
        send_mail(
            subject="Password Reset",
            message=f"Dear {subscriber.first_name},\n\nYour password has been reset. " +
            f"Your temporary password is: {temp_password}\n\nPlease log in and change your password immediately.",
            from_email="no-reply@example.com",
            recipient_list=[subscriber.email],
        )

        return Response({"message": "A temporary password has been sent to your email."})