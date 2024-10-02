from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from rest_framework import status
from inventory.models import Item

User = get_user_model()


class ItemCRUDTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="test23", email="test@test.com", password="testpass")

        self.item = Item.objects.create(name="Gloves")

    def test_list_items(self):
        token = RefreshToken.for_user(self.user).access_token
        headers = {'Authorization': f'Bearer {token}'}

        res = self.client.get(
            reverse("items-list"),
            headers=headers,
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_item(self):
        token = RefreshToken.for_user(self.user).access_token
        headers = {'Authorization': f'Bearer {token}'}
        payload = {"name": "test item"}

        res = self.client.post(
            reverse("items-list"),
            data=payload,
            headers=headers,
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_retrive_item(self):
        token = RefreshToken.for_user(self.user).access_token
        headers = {'Authorization': f'Bearer {token}'}

        res = self.client.get(
            reverse("items-detail", kwargs={"pk": self.item.pk}),
            headers=headers,
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        token = RefreshToken.for_user(self.user).access_token
        headers = {'Authorization': f'Bearer {token}'}
        payload = {"name": "test item"}

        res = self.client.patch(
            reverse("items-detail", kwargs={"pk": self.item.pk}),
            data=payload,
            headers=headers,
            format='json',
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
