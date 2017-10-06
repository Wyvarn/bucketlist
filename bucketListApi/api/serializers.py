from rest_framework.serializers import ModelSerializer
from .models import BucketList


class BucketListSerializer(ModelSerializer):
    """
    Serializer to map the Model instance to JSON
    """

    class Meta:
        model = BucketList
        fields = ("id", "name", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")
