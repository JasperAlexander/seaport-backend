from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer


class GetTransactionsView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class GetTransactionView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
