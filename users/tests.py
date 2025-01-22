from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='super@gmail.com', is_staff=True, is_superuser=True,)
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """ Тест создания пользователя"""
        url = reverse('users:register')
        data = {
            'email': 'student@mail.ru',
            'password': 'qwe123'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            User.objects.all().count(), 2
        )

    def test_user_retrieve(self):
        """ Тест просмотра пользователя"""
        url = reverse('users:user_retrieve', args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('email'), self.user.email
        )

    def test_user_list(self):
        """Тест просмотра списка пользователей"""
        url = reverse('users:list')
        response = self.client.get(url)
        result = [
            {
                'avatar': None,
                'city': None,
                'email': self.user.email,
                'first_name': None,
                'id': self.user.id,
                'last_name': None,
                'password': '',
                'phone': None
            }
        ]
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_user_update(self):
        """ Тест изменения пользователя"""
        url = reverse('users:user_update', args=(self.user.pk,))
        data = {
            'first_name': 'David',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('first_name'), 'David'
        )

    def test_user_delete(self):
        """ Тест удаления пользователя"""
        url = reverse('users:user_delete', args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            User.objects.all().count(), 0
        )