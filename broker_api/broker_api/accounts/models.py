from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, related_name='accounts')
    account_name = models.CharField(max_length=200)
    buying_power = models.IntegerField(default=0)
    initial_cash = models.PositiveIntegerField()

    class Meta:
        unique_together=('user', 'account_name')

    def save(self, *args, **kwargs):
        self.buying_power = self.buying_power + self.initial_cash
        super().save(*args, **kwargs)

    def __str__(self):
        return self.account_name

