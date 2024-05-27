from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core import models

class AccountTests(APITestCase):

    def test_get_list(self):

        url = reverse('programmerView')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Programmer.objects.count(), 200)
        self.assertEqual(models.Programmer.objects.get().name, 'DabApps')
