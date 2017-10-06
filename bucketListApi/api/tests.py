from django.test import TestCase

from .models import BucketList


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

