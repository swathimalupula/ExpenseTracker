# Generated by Django 5.1.7 on 2025-03-20 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_expense_category_remove_expense_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
    ]
