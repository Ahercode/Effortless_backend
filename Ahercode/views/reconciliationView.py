from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response

class ReconciliationView(APIView):
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
                WHEN transactions.transaction_type = 'Income' AND transactions.debit != 0.00 THEN account_details.note
                WHEN transactions.transaction_type = 'Expense' AND transactions.debit = 0.00 THEN account_details.note
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
            LOWER(transactions.transaction_type) IN ('income', 'expense', 'journal');
        """

        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return Response(results)