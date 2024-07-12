from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Transfer

def home(request):
    return render(request, 'customers/home.html')

def customers_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customers_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

def transfer_money(request, pk):
    from_customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        to_customer_id = request.POST.get('to_customer')
        amount = int(request.POST.get('amount'))
        to_customer = get_object_or_404(Customer, pk=to_customer_id)
        if from_customer.balance >= amount:
            from_customer.balance -= amount
            to_customer.balance += amount
            from_customer.save()
            to_customer.save()
            Transfer.objects.create(from_customer=from_customer, to_customer=to_customer, amount=amount)
            return redirect('customers_list')
    customers = Customer.objects.exclude(pk=pk)
    return render(request, 'customers/transfer_money.html', {'from_customer': from_customer, 'customers': customers})
