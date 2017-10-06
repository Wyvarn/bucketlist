from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField
from .models import BucketList
from django.contrib.auth.models import User


class BucketListSerializer(ModelSerializer):
    """
    Serializer to map the Model instance to JSON
    """
    owner = ReadOnlyField(source="owner.username")

    class Meta:
        model = BucketList
        fields = ("id", "name", "owner", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")


class UserSerializer(ModelSerializer):
    """User serializer to aid in authentication and authorization"""

    bucketlists = PrimaryKeyRelatedField(many=True, queryset=BucketList.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "bucketlist")
