from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

from main_app.models import Toy, Cat, Feeding

User = get_user_model()


class AuthenticationTests(APITestCase):
    pass


class CatTests(APITestCase):
    pass


class FeedingTests(APITestCase):
    pass