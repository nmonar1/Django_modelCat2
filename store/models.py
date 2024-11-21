from django.db import models

# Create your models here

class Customer(models.Model):
    name = models.CharField(max_length=255)  #customer's full name
    email = models.EmailField(unique=True)  #this  each email is unique

    def __str__(self):
        return self.name  # Display name when object is queried

class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders"
    )  # A customer can have multiple orders
    order_date = models.DateTimeField(auto_now_add=True)  # Auto-set to now when created
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total cost

    def __str__(self):
        return f"Order #{self.id} by {self.customer.name}"
