from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from rest_framework import status

from django.contrib.auth.models import User
from apps.loc.models import Location, City, Country, Region

from .models import (
    Category,
    Thing,
    Image,
    UserProfile,
    Trade,
    Feedback,           
)

from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

class CategoryTests(APITestCase):
    def test_create_category(self):
        url = "/api/v1/category/"
        data = {"name": "Test"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, "Test")


class UserProfileTests(APITestCase):
    def test_create_user_profile(self):
        url = "/api/v1/userprofile/"

        country = Country.objects.create(name="TestCountry")
        region = Region.objects.create(name="TestRegion", country=country)
        city = City.objects.create(name="TestCity", region=region)
        location = Location.objects.create(country=country, region=region, city=city )

        user = User.objects.create_user(username="test_user", password="password")

        data = {"user": user.id, "location": location.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(UserProfile.objects.get().user, user)
        self.assertEqual(UserProfile.objects.get().location, location)


class ThingTests(APITestCase):
    def test_create_thing(self):
        user = User.objects.create_user(username="test_user", password="password")
        category = Category.objects.create(name="Test Category")
        image = Image.new("RGB", (100, 100))
        image_file = SimpleUploadedFile("test_image.jpg", image.tobytes())

        url = "/api/v1/thing/"

        # Передаем SimpleUploadedFile напрямую в теле запроса
        data = {
            "name": "Test Thing",
            "description": "Test Description",
            "category": category.id,
            "owner": user.id,
            "image": image_file,  # Просто передаем объект SimpleUploadedFile
        }

        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Thing.objects.count(), 1)
        self.assertEqual(Thing.objects.get().name, "Test Thing")
        self.assertEqual(Thing.objects.get().description, "Test Description")
        self.assertEqual(Thing.objects.get().category, category)
        self.assertEqual(Thing.objects.get().owner, user)


class TradeTests(APITestCase):
    def test_create_trade(self):
        user_A = User.objects.create_user(username="user_A", password="password")
        user_B = User.objects.create_user(username="user_B", password="password")
        category = Category.objects.create(name="Test Category")
        thing = Thing.objects.create(
            name="Test Thing",
            description="Test Description",
            category=category,
            owner=user_A,
        )
        url = "/api/v1/trade/"
        data = {
            "thing": thing.id,
            "participant_A": user_A.id,
            "participant_B": user_B.id,
        }
        self.client.force_authenticate(user=user_A)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trade.objects.count(), 1)
        self.assertEqual(Trade.objects.get().thing, thing)
        self.assertEqual(Trade.objects.get().participant_A, user_A)
        self.assertEqual(Trade.objects.get().participant_B, user_B)


class FeedbackTests(APITestCase):
    def test_create_feedback(self):
        user_A = User.objects.create_user(username="user_A", password="password")
        user_B = User.objects.create_user(username="user_B", password="password")
        category = Category.objects.create(name="Test Category")
        thing = Thing.objects.create(
            name="Test Thing",
            description="Test Description",
            category=category,
            owner=user_A,
        )
        trade = Trade.objects.create(
            thing=thing, participant_A=user_A, participant_B=user_B
        )
        url = "/api/v1/feedback/"
        data = {"text": "Test Feedback", "rating": 5, "trade": trade.id}
        self.client.force_authenticate(user=user_B)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 1)
        self.assertEqual(Feedback.objects.get().text, "Test Feedback")
        self.assertEqual(Feedback.objects.get().rating, 5)
        self.assertEqual(Feedback.objects.get().trade, trade)
