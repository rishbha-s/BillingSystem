from django.apps import apps
from django.db import models
from .models import Login  # Assuming your Login model is in the same app


class Customer(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    customer_id = models.BigIntegerField(primary_key=True)
    email_id = models.CharField(max_length=50, unique=True)
    login = models.OneToOneField(apps.get_model('billing', 'Login'), on_delete=models.CASCADE, related_name='customer', null=True, blank=True)

# Create your models here.
# billing/models.py

class Login(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    email_id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.email_id

class Customer(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone_no = models.BigIntegerField()
    customer_id = models.BigIntegerField(primary_key=True)
    email_id = models.CharField(max_length=50, unique=True)
    login = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='customer', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.customer_id}"

class Services(models.Model):
    service_id = models.BigIntegerField(primary_key=True)
    service_type = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return f"{self.service_type} - {self.service_id}"

class Invoice(models.Model):
    invoice_id = models.BigIntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='invoices')
    total_amt = models.FloatField()
    in_date = models.DateField()

    def __str__(self):
        return f"Invoice {self.invoice_id} - Total Amount: {self.total_amt}"

class Payments(models.Model):
    payment_id = models.BigIntegerField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='payments')
    amount = models.FloatField()
    balance_due = models.FloatField()

    def __str__(self):
        return f"Payment {self.payment_id} - Amount: {self.amount}"
    

    # customers/models.py



