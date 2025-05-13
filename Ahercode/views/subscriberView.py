
from django.db import connection
from rest_framework import generics
from django.core.mail import send_mail
from Ahercode.models import Subscribers
from Ahercode.serializers import SubscriberSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from Ahercode.models import Subscribers
from django.db.models import Sum, Max, Case, When, Value, CharField, IntegerField, F, DecimalField
from rest_framework.views import APIView
from rest_framework.response import Response
from Ahercode.models import Transactions, Subscribers


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


class SubscriberTransactionSummaryView(APIView):
    """
    API view to return transaction summary for each subscriber.
    """

    def get(self, request):
        
        results = Subscribers.objects.annotate(
            income_count=Sum(
                Case(
                    When(transactions__transaction_type='Income', transactions__credit__gt=0, then=1),
                    default=0,
                    output_field=IntegerField(),
                )
            ),
            income_amount=Sum(
                Case(
                    When(transactions__transaction_type='Income', then=F('transactions__credit')),
                    default=0,
                    output_field=DecimalField(max_digits=10, decimal_places=2),
                )
            ),
            last_incomedate=Max(
                Case(
                    When(transactions__transaction_type='Income', then=F('transactions__transaction_date')),
                    default=None,
                )
            ),
            expense_count=Sum(
                Case(
                    When(transactions__transaction_type='Expense', transactions__debit__gt=0, then=1),
                    default=0,
                    output_field=IntegerField(),
                )
            ),
            expense_amount=Sum(
                Case(
                    When(transactions__transaction_type='Expense', then=F('transactions__debit')),
                    default=0,
                    output_field=DecimalField(max_digits=10, decimal_places=2),
                )
            ),
            last_expensedate=Max(
                Case(
                    When(transactions__transaction_type='Expense', then=F('transactions__transaction_date')),
                    default=None,
                )
            ),
            debit_count=Sum(
                Case(
                    When(transactions__transaction_type='Journal', transactions__debit__gt=0, then=1),
                    default=0,
                    output_field=IntegerField(),
                )
            ),
            credit_count=Sum(
                Case(
                    When(transactions__transaction_type='Journal', transactions__credit__gt=0, then=1),
                    default=0,
                    output_field=IntegerField(),
                )
            ),
            debit_amount=Sum(
                Case(
                    When(transactions__transaction_type='Journal', then=F('transactions__debit')),
                    default=0,
                    output_field=DecimalField(max_digits=10, decimal_places=2),
                )
            ),
            credit_amount=Sum(
                Case(
                    When(transactions__transaction_type='Journal', then=F('transactions__credit')),
                    default=0,
                    output_field=DecimalField(max_digits=10, decimal_places=2),
                )
            ),
            last_journaldate=Max(
                Case(
                    When(transactions__transaction_type='Journal', then=F('transactions__transaction_date')),
                    default=None,
                )
            ),
        ).values(
            'id',
            'company_name',
            'income_count',
            'income_amount',
            'last_incomedate',
            'expense_count',
            'expense_amount',
            'last_expensedate',
            'debit_count',
            'credit_count',
            'debit_amount',
            'credit_amount',
            'last_journaldate',
        )

        return Response(results)   



class SubscriberTransactionDetailsView(APIView):
    """
    API view to execute a custom SQL query and return transaction details.
    """

    def get(self, request):
        query = """
        SELECT DISTINCT
            transactions.subscriber_id,
            transactions.transaction_date,
            transactions.reference_number,
            transactions.transaction_type,
            transactions.description,
            CASE
                WHEN transactions.debit != 0.00 THEN transactions.debit
                WHEN transactions.credit != 0.00 THEN transactions.credit
                ELSE 0.00
            END AS amount,
            CASE
                WHEN transactions.transaction_type = 'Income' AND transactions.debit = 0.00 THEN accounts.account
                WHEN transactions.transaction_type = 'Expense' AND transactions.debit != 0.00 THEN accounts.account
                WHEN transactions.transaction_type = 'Journal' THEN accounts.account
                ELSE NULL
            END AS account,
            CONCAT(parties.last_name, ' ', parties.first_name) AS name,
            parties.type AS party_type,
            inExDetails.status
        FROM
            Ahercode_transactions AS transactions
        LEFT JOIN
            Ahercode_account AS accounts
            ON transactions.account_id = accounts.id
        LEFT JOIN
            Ahercode_account_details AS account_details
            ON transactions.account_id = account_details.id
        LEFT JOIN
            Ahercode_inExDetails AS inExDetails
            ON transactions.reference_number = inExDetails.reference_number
        LEFT JOIN
            Ahercode_party AS parties
            ON inExDetails.party_id = parties.id
        WHERE
            (transactions.transaction_type = 'Income' AND transactions.credit > 0)
            OR (transactions.transaction_type = 'Expense' AND transactions.debit > 0)
            OR (transactions.transaction_type = 'Journal');
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return Response(results)