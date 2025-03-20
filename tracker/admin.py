from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount', 'category', 'date']
    list_filter = ['category', 'date']
    search_fields = ['name', 'category']
