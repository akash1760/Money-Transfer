from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Transfer(models.Model):
    from_customer = models.ForeignKey(Customer, related_name='sent_transfers', on_delete=models.CASCADE)
    to_customer = models.ForeignKey(Customer, related_name='received_transfers', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
