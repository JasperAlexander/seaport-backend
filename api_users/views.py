from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class GetUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
