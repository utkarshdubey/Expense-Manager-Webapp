from django.db import models

class ExpenseList(models.Model):
    amount = models.FloatField()
    title = models.TextField()
