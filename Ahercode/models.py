

from django.db import models

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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Account(models.Model):
    account_header = models.CharField(max_length=100, null=True, blank=True)
    account = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    line = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

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
    status = models.CharField(max_length=100, default="unreconciled")
    posted = models.BooleanField(default=False)

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

    def save(self, *args, **kwargs):
        if not self.bach_id:  # Generate only if batch_id is empty
            last_transaction = Transactions.objects.filter(
                subscriber=self.subscriber
            ).order_by('-id').first()

            if last_transaction and last_transaction.bach_id:
                last_number = int(last_transaction.bach_id.split('-')[1])  # Extract last part
                next_number = last_number + 1
            else:
                next_number = 1  # First transaction for this subscriber

            self.bach_id = f"{self.subscriber.id:05d}-{next_number:05d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference_number