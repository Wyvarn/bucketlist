from django.db import models
from django.db.models import CharField, DateTimeField


class BucketList(models.Model):
    """
    Bucket list model
    """
    name = CharField(max_length=255, blank=False, unique=True)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)

    def __str__(self):
        """
        return Human readable format of the bucket list model instance
        :returns str
        """
        return "{}".format(self.name)
