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


class Subscriber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alternative_email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    description = models.TextField()
    tax_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Account(models.Model):
    account_header = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    line = models.CharField(max_length=50)

    def __str__(self):
        return self.account_header


class Party(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    expense_count = models.IntegerField()
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    alternate_email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Journal(models.Model):
    date = models.DateField()
    journal_number = models.CharField(max_length=100)
    subscriberId = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    note = models.TextField()
    prepared_by = models.CharField(max_length=100)

    def __str__(self):
        return self.journal_number


class JournalDetails(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=100)

    def __str__(self):
        return self.reference_number


class Transactions(models.Model):
    transaction_type = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    date = models.DateField()
    reference_number = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    outstanding = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.reference_number