from django.test import TestCase

from .models import BucketList
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from rest_framework import status


class ModelTestCase(TestCase):
    """Test case defining Bucketlist models"""

    def setUp(self):
        """Define test client and other test variables"""
        self.bucketlist_name = "Awesome BucketList"
        self.bucketlist = BucketList(name=self.bucketlist_name)

    def test_model_can_create_a_bucket_list(self):
        """Test the bucketlist model can create a bucketlist"""
        old_count = BucketList.objects.count()
        self.bucketlist.save()
        new_count = BucketList.objects.count()
        self.assertNotEqual(old_count, new_count, "Expected counts to be different")


class ViewTestCase(TestCase):
    """Test suite for api views"""

    def setUp(self):
        """Define test client and other test variables"""
        self.client = APIClient()
        self.bucketlist_data = {"name": "Go to the Moon"}
        self.response = self.client.post(
            reverse("create"),
            self.bucketlist_data,
            format="json"
        )

    def test_api_can_create_a_bucket_list(self):
        """Test that api can create a bucket list"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)