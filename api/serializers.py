from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import BucketList


class BucketListSerializer(ModelSerializer):
    """
    Serializer to map the Model instance to JSON
    """
    owner = ReadOnlyField(source="owner.username")

    class Meta:
        model = BucketList
        fields = ("id", "name", "owner", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")

