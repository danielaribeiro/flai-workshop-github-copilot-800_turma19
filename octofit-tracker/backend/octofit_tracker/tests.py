from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Team, UserProfile


class BasicAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='test-team')
        self.user = UserProfile.objects.create(name='Tester', email='tester@example.com', team=self.team)

    def test_users_list(self):
        url = reverse('userprofile-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(len(resp.data) >= 1)

    def test_api_root(self):
        url = reverse('api-root')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
