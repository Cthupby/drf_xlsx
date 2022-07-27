from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['client_name', 'client_org', 
                  'number', 'amount', 
                  'date', 'service']
