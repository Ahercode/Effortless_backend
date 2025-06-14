

import os
from django.db import models, transaction

# Create your models here.


from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Subscribers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alternative_email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    description = models.TextField(blank=True, null=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=100, default="pending")
    password = models.CharField(max_length=100, default="")
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SubscriberUsers(models.Model):
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user_id

class Account(models.Model):
    account_header = models.CharField(max_length=100, null=True, blank=True)
    account = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    line = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.account_header

class AccountDetails(models.Model):
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Ahercode_account_details'

    def __str__(self):
        return self.account


class Party(models.Model):
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE, null=True, blank=True)  # Allow null values
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    alternate_email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class JournalHeaders(models.Model):
    transaction_date = models.DateField()
    journal_number = models.CharField(max_length=100)
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    note = models.TextField(blank=True, null=True)
    prepared_by = models.CharField(max_length=100)
    posted = models.BooleanField(default=False)
    def __str__(self):
        return self.journal_number


class Journals(models.Model):
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    journal = models.ForeignKey(JournalHeaders, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=100, default="journal")
    debit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_date = models.DateField()


    def __str__(self):
        return self.reference_number

class InExDetails(models.Model):
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    reference_number = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=100)
    selected_bank = models.IntegerField(default=0)
    status = models.CharField(max_length=100, default="unreconciled")
    posted = models.BooleanField(default=False)
    tag = models.ForeignKey('Tags', on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.reference_number

class Transactions(models.Model):
    bach_id = models.CharField(max_length=100, blank=True, null=True)
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_date = models.DateField()
    reference_number = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    debit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tag = models.ForeignKey('Tags', on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Use a transaction to ensure consistency for grouped transactions
        with transaction.atomic():
            if not self.bach_id:  # Generate only if batch_id is empty
                # Check if there are other transactions being saved together
                grouped_transactions = Transactions.objects.filter(
                    subscriber=self.subscriber,
                    transaction_date=self.transaction_date,
                    reference_number=self.reference_number,
                ).order_by('-id')

                if grouped_transactions.exists():
                    # Use the same batch ID for grouped transactions
                    self.bach_id = grouped_transactions.first().bach_id
                else:
                    # Get the last transaction for the same subscriber
                    last_transaction = Transactions.objects.filter(
                        subscriber=self.subscriber
                    ).order_by('-id').first()

                    if last_transaction and last_transaction.bach_id:
                        last_number = int(last_transaction.bach_id.split('-')[1])  # Extract last part
                        next_number = last_number + 1
                    else:
                        next_number = 1  # First transaction for this subscriber

                    # Generate the new batch ID
                    self.bach_id = f"{self.subscriber.id:05d}-{next_number:05d}"

            super().save(*args, **kwargs)

    def __str__(self):
        return self.reference_number

class CalendarEvents(models.Model):
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE, related_name='calendar_events')
    title = models.CharField(max_length=100)
    start_date= models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, default="")
    frequency = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class CRM(models.Model):
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    date = models.DateField()
    note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, default="")
    file = models.FileField(upload_to='uploads/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Handle file replacement during updates
        if self.pk:
            old_instance = CRM.objects.get(pk=self.pk)
            if old_instance.file and old_instance.file != self.file:
                if os.path.isfile(old_instance.file.path):
                    os.remove(old_instance.file.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the associated file when the CRM instance is deleted
        if self.file and os.path.isfile(self.file.path):
            os.remove(self.file.path)
        super().delete(*args, **kwargs)
        
        
    def __str__(self):
        return self.note


class Assets(models.Model):
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    expense = models.ForeignKey(InExDetails, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    serial_number = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.serial_number


class Tips(models.Model):
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.date


class Tags(models.Model):
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name