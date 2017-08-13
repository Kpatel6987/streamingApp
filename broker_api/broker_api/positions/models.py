from django.db import models
from ..accounts.models import Account

class Position(models.Model):
    account = models.ForeignKey(Account, related_name='positions')
    underlying = models.CharField(max_length=10)
    quantity = models.IntegerField()
    cost = models.IntegerField()

    class Meta:
        unique_together=('account', 'underlying')

    def __str__(self):
        return self.underlying
