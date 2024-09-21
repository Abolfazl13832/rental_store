from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, Q
from django.db.models.functions import Coalesce


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

    @classmethod
    def get_balance(cls):
        positive_transactions = Coalesce(Sum('transactions__amount', filter=Q(transactions__transaction_type=1)), 0)
        negative_transactions = Coalesce(
            Sum('transactions__amount', filter=Q(transactions__transaction_type__in=[2, 3])), 0)

        user = User.objects.annotate(balance=positive_transactions - negative_transactions)

    def __str__(self):
        return f"{self.user} - {self.get_transaction_type_display()} - {self.amount}"


class UserBalance(models.Model):
    user = models.ForeignKey(User, related_name="balance_records", on_delete=models.RESTRICT)
    balance = models.BigIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def recorder_user_balance(cls, user):
        positive_transactions = Sum('amount', filter=Q(transaction_type=1))
        negative_transactions = Sum('amount', filter=Q(transaction_type__in=[2, 3]))
        user_balance = user.transactions.all().aggregate(
            balance=Coalesce(positive_transactions, 0) - Coalesce(negative_transactions, 0)
        )
        instance = cls.objects.create(user=user, balance=user_balance['balance'])
        return instance

    @classmethod
    def record_total_user_balance(cls):  #برگرداندن موجودی کیف پول برای همه
        for user in User.objects.all():
            record = cls.recorder_user_balance(user)

    def __str__(self):
        return f"{self.user} -{self.balance}-{self.created_date}"
