from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date

from main_app.models import Toy, Cat, Feeding

User = get_user_model()


class AuthenticationTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'testuser',
            'password': 'testpass123',
            'email': 'test@test.com'
        }
        self.user = User.objects.create_user(**self.user_data)
        self.auth_token = str(RefreshToken.for_user(self.user).access_token)

    def test_user_registration(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'password': 'newpass123',
            'email': 'new@test.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertTrue(User.objects.filter(username='newuser').exists())


class CatTests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@test.com'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='otherpass123',
            email='other@test.com'
        )

        # Get JWT token
        self.client = APIClient()
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        }, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Create test data
        self.cat = Cat.objects.create(
            name='TestCat',
            breed='TestBreed',
            description='Test Description',
            age=3,
            user=self.user
        )
        self.toy = Toy.objects.create(
            name='TestToy',
            color='Red'
        )

    def test_create_cat(self):
        data = {
            'name': 'NewCat',
            'breed': 'NewBreed',
            'description': 'New Description',
            'age': 2
        }
        response = self.client.post(reverse('cat-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cat.objects.count(), 2)
        self.assertEqual(Cat.objects.get(name='NewCat').user, self.user)

    def test_get_cat_detail(self):
        response = self.client.get(reverse('cat-detail', kwargs={'id': self.cat.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cat']['name'], 'TestCat')
        self.assertIn('toys_not_associated', response.data)
        self.assertIn('fed_for_today', response.data['cat'])

    def test_update_cat(self):
        data = {
            'name': 'UpdatedCat',
            'breed': 'UpdatedBreed',
            'description': 'Updated Description',
            'age': 4
        }
        response = self.client.put(
            reverse('cat-detail', kwargs={'id': self.cat.id}),
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cat.refresh_from_db()
        self.assertEqual(self.cat.name, 'UpdatedCat')
        self.assertEqual(self.cat.description, 'Updated Description')

    def test_add_toy_to_cat(self):
        response = self.client.post(
            reverse('add-toy-to-cat', kwargs={
                'cat_id': self.cat.id,
                'toy_id': self.toy.id
            })
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.toy in self.cat.toys.all())


class FeedingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@test.com'
        )
        self.client = APIClient()
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass123'
        }, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.cat = Cat.objects.create(
            name='TestCat',
            breed='TestBreed',
            description='Test Description',
            age=3,
            user=self.user
        )

    def test_create_feeding(self):
        data = {
            'date': str(date.today()),
            'meal': 'B'
        }
        response = self.client.post(
            reverse('feeding-list-create', kwargs={'cat_id': self.cat.id}),
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feeding.objects.count(), 1)
        self.assertEqual(Feeding.objects.first().cat, self.cat)
        self.assertEqual(Feeding.objects.first().meal, 'B')

    def test_fed_for_today(self):
        # Create all meals for today
        meals = ['B', 'L', 'D']
        for meal in meals:
            Feeding.objects.create(
                cat=self.cat,
                date=date.today(),
                meal=meal
            )

        # Get cat details to check fed_for_today
        response = self.client.get(reverse('cat-detail', kwargs={'id': self.cat.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['cat']['fed_for_today'])

    def test_list_feedings(self):
        # Create test feeding
        Feeding.objects.create(
            cat=self.cat,
            date=date.today(),
            meal='B'
        )
        response = self.client.get(
            reverse('feeding-list-create', kwargs={'cat_id': self.cat.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['meal'], 'B')

    def test_update_feeding(self):
        feeding = Feeding.objects.create(
            cat=self.cat,
            date=date.today(),
            meal='B'
        )
        data = {
            'date': str(date.today()),
            'meal': 'D'
        }
        response = self.client.put(
            reverse('feeding-detail', kwargs={
                'cat_id': self.cat.id,
                'id': feeding.id
            }),
            data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        feeding.refresh_from_db()
        self.assertEqual(feeding.meal, 'D')