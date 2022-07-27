from rest_framework import serializers
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(max_length=100)
    client_org = serializers.CharField(max_length=100)
    number = serializers.IntegerField()
    amount = serializers.IntegerField(min_value=0)
    date = serializers.DateField(format='%d%m%Y')
    service = serializers.CharField()

    class Meta:
        model = Bill
        fields = '__all__'
