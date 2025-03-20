from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Rent', 'Rent'),
        ('Entertainment', 'Entertainment'),
        ('Utilities', 'Utilities'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default="Unknown Expense")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount} ({self.category})"
