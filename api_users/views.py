from rest_framework import generics
from .models import User
from .serializers import UserReadSerializer, UserWriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import UsersCursorPagination


class GetUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
    pagination_class = UsersCursorPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["address"]


class GetUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserReadSerializer
    lookup_field = "username"


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserWriteSerializer
