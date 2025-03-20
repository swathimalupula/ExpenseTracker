from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_expense, name='add_expense'),
    path('', views.expense_list, name='expense_list'),
    path('report/', views.monthly_report, name='monthly_report'),
    
]
