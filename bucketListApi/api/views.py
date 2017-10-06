from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketListSerializer
from .models import BucketList


class CreateView(generics.ListCreateAPIView):
    """
    This defines the create behaviour for our api view
    The ListCreateAPIView is a generic view which provides GET (list all) and POST method handlers
    """
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        """
        Save the post data when create a new bucket list item
        :param serializer serializer to map model object to JSON
        """
        serializer.save()
