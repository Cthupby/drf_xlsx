from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

import base64

from .serializers import BillSerializer
from .models import Bill


class BillList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all bills
    '''
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'client_name', 'client_org']

    def perform_create(self, serializer):
        serializer.save()
