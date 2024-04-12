from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework import status

from django.contrib.auth.models import User

from .models import (
    Category,
    Thing,
    Image,
    UserProfile,
    Trade,
    Feedback,           
)

from .views import (
    UserViewSet,
    CategoryViewSet,
    ThingViewSet,
    UserProfileViewSet,
    TradeViewSet,
    FeedbackViewSet,
    ImageViewSet
)

class CategoryTests(APITestCase):
    def test_create_thing(self):
        url = "/api/v1/category/"
        data = {"name": "Test"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, "Test")
