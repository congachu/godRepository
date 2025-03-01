from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, mixins
# Create your views here.

class UserView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')
