from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Import login_required
from .models import Expense
from .forms import ExpenseForm
from django.db.models import Sum
import datetime

@login_required  # Ensure user is logged in
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Only logged-in users can add expenses
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})  # Removed 'templates/' from path

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense_list.html', {'expenses': expenses})

@login_required
def monthly_report(request):
    today = datetime.date.today()
    expenses = Expense.objects.filter(user=request.user, date__month=today.month)
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'monthly_report.html', {'expenses': expenses, 'total': total})
