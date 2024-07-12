from customers.models import Customer

for i in range(10):
    Customer.objects.create(name=f'Customer {i+1}', email=f'customer{i+1}@example.com', balance=100.00)
