from django.db import models


class Bill(models.Model):
    client_name = models.CharField(max_length=100)
    client_org = models.CharField(max_length=100)
    number = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateField()
    service = models.TextField()
