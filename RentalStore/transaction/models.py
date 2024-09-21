from django.contrib.auth.models import User
from django.db import models


class Transaction(models.Model):
    CHARGE = 1
    PURCHASE = 2
    WITHDRAW = 3
    TRANSACTION_CHOICES = (
        (CHARGE, 'Charge'),
        (PURCHASE, 'Purchase'),
        (WITHDRAW, 'Withdraw'),
    )
    user = models.ForeignKey(User, related_name="transactions", on_delete=models.RESTRICT)
    transaction_type = models.PositiveSmallIntegerField(choices=TRANSACTION_CHOICES, default=CHARGE)
    amount = models.BigIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.get_transaction_type_display()} - {self.amount}"


class UserBalance(models.Model):
    user = models.ForeignKey(User, related_name="balance_records", on_delete=models.RESTRICT)
    balance = models.BigIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -{self.balance}-{self.created_date}"

