from rest_framework import generics
from .models import Contract
from .serializers import ContractSerializer


class GetContractsView(generics.ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class GetContractView(generics.RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
