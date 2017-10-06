from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import BucketListSerializer, UserSerializer
from .models import BucketList
from .permissions import IsOwner
from django.contrib.auth.models import User


class CreateView(generics.ListCreateAPIView):
    """
    This defines the create behaviour for our api view
    The ListCreateAPIView is a generic view which provides GET (list all) and POST method handlers
    """
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """
        Save the post data when create a new bucket list item
        :param serializer serializer to map model object to JSON
        """
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Handles the GET, PUT, DELETE methods"""
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = permissions.IsAuthenticated, IsOwner


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
