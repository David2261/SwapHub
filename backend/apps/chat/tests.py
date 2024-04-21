from rest_framework.test import APITestCase
from rest_framework import status

from .models import Dialog, Message
from django.contrib.auth.models import User


class DialogTests(APITestCase):
    def test_create_dialog(self):
        url = "/api/v1/dialog/"
        user_A = User.objects.create_user(username="test_user_A", password="password")
        user_B = User.objects.create_user(username="test_user_B", password="password")
        data = {"user_A": user_A.id, "user_B": user_B.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dialog.objects.count(), 1)
        self.assertEqual(Dialog.objects.get().user_A, user_A)
        self.assertEqual(Dialog.objects.get().user_B, user_B)


class MessageTests(APITestCase):
    def test_create_message(self):
        url = "/api/v1/message/"
        user_A = User.objects.create_user(username="test_user_A", password="password")
        user_B = User.objects.create_user(username="test_user_B", password="password")
        dialog = Dialog.objects.create(user_A=user_A, user_B=user_B)
        
        user = User.objects.create_user(username="test_user", password="password")
        data = {"dialog": dialog.id, "user": user.id, "text": "test"}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().text, "test")
        self.assertEqual(Message.objects.get().dialog, dialog)
        self.assertEqual(Message.objects.get().user, user)
