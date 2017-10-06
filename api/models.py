from django.db import models
from django.db.models import CharField, DateTimeField, ForeignKey, CASCADE
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


class BucketList(models.Model):
    """
    Bucket list model
    """
    name = CharField(max_length=255, blank=False, unique=True)
    owner = ForeignKey("auth.User", related_name="bucketlists", on_delete=CASCADE)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)

    def __str__(self):
        """
        return Human readable format of the bucket list model instance
        :returns str
        """
        return "{}".format(self.name)


@receiver(signal=post_save, sender=User)
def create_auth_token(sender, instance=None, created=False,**kwargs):
    """Receiver handles token creation immediately a user is created"""
    if created:
        Token.objects.create(user=instance)
