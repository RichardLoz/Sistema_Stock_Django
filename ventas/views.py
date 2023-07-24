from django.shortcuts import render
from .models import *

def list_invoices(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice.html', {'invoices':invoices })
