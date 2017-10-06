from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import BucketList


class ModelTestCase(TestCase):
    """Test case defining Bucketlist models"""

    def setUp(self):
        """Define test client and other test variables"""
        self.bucketlist_name = "Awesome BucketList"
        user = User.objects.create_user(username="SpongeBob")
        self.bucketlist = BucketList(name=self.bucketlist_name, owner=user)

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
        user = User.objects.create_user(username="SpongeBob")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.bucketlist_data = {"name": "Go to the Moon"}
        self.response = self.client.post(reverse("create"), self.bucketlist_data,
                                         format="json")

    def test_api_can_create_a_bucket_list(self):
        """Test that api can create a bucket list"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_authorization_is_enforced(self):
        """Test the api has user authorization"""
        new_client = APIClient()
        res = new_client.get("/bucketlists/", kwargs={"pk": 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_bucket_list(self):
        """Test that the api can get a bucket list given its name"""
        bucketlist = BucketList.objects.get(id=1)
        res = self.client.get(reverse("details", kwargs={"pk": bucketlist.id}), format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, bucketlist)

    def test_api_can_update_a_bucket_list(self):
        """Test that the API can update a bucket list"""
        bucketlist = BucketList.objects.get()
        change_bucketlist = {"name": "Visit Paris"}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = BucketList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
