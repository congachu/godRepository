from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, mixins
# Create your views here.

class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
