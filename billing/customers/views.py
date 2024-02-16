from django.shortcuts import render

from .models import Customer, Services, Invoice, Payments

def index(request):
    customers = Customer.objects.all()
    services = Services.objects.all()
    invoices = Invoice.objects.all()
    payments = Payments.objects.all()
    return render(request, 'billing/index.html', {'customers': customers, 'services': services, 'invoices': invoices, 'payments': payments})