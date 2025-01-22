from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User
from users_tests.models import Test, Question, Answer


class TestTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='super@gmail.com', is_staff=True, is_superuser=True,)
        self.client.force_authenticate(user=self.user)
        self.test = Test.objects.create(name='Exemple 1', autor=self.user,)

    def test_test_create(self):
        """ Тест создания теста"""
        url = reverse('users_tests:tests-list')
        data = {
            'name': 'Exemple 2',

        }
        response = self.client.post(url, data=data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Test.objects.all().count(), 2
        )

    def test_test_retrieve(self):
        """ Тест просмотра теста"""
        url = reverse('users_tests:tests-detail', args=(self.test.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.test.name
        )

    def test_test_list(self):
        """ Тест просмотра списка тестов"""
        url = reverse('users_tests:tests-list')
        response = self.client.get(url)
        result = [
            {
                'id': self.test.id,
                'name': self.test.name,
                'body': None,
                'autor': self.user.id,
                'course': None,
                'lesson': None
            }
        ]
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_test_update(self):
        """ Тест изменения теста"""
        url = reverse('users_tests:tests-detail', args=(self.test.pk,))
        data = {
            'name': 'Exemple',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Exemple'
        )

    def test_test_delete(self):
        """ Тест удаления теста"""
        url = reverse('users_tests:tests-detail', args=(self.test.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Test.objects.all().count(), 0
        )


class QuestionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='super@gmail.com', is_staff=True, is_superuser=True, )
        self.client.force_authenticate(user=self.user)
        self.test = Test.objects.create(name='Exemple 1', autor=self.user, )
        self.question = Question.objects.create(name='Question 1', test=self.test, autor=self.user, )

    def test_test_create(self):
        """ Тест создания вопроса"""
        url = reverse('users_tests:questions-list')
        data = {
            'name': 'Question 2',
            'test': self.test.id,
            'autor': self.user.id
        }
        response = self.client.post(url, data=data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Question.objects.all().count(), 2
        )

    def test_question_retrieve(self):
        """ Тест просмотра вопроса"""
        url = reverse('users_tests:questions-detail', args=(self.question.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.question.name
        )

    def test_question_list(self):
        """ Тест просмотра списка вопросов"""
        url = reverse('users_tests:questions-list')
        response = self.client.get(url)
        result = [
            {
                'id': self.question.id,
                'name': self.question.name,
                'image': None,
                'test': self.question.test.pk,
                'autor': self.user.id
            }
        ]
        data = response.json()
        #print(data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_question_update(self):
        """ Тест изменения вопроса"""
        url = reverse('users_tests:questions-detail', args=(self.question.pk,))
        data = {
            'name': 'Question',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Question'
        )

    def test_question_delete(self):
        """ Тест удаления вопроса"""
        url = reverse('users_tests:questions-detail', args=(self.question.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Question.objects.all().count(), 0
        )


class AnswerTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='super@gmail.com', is_staff=True, is_superuser=True, )
        self.client.force_authenticate(user=self.user)
        self.test = Test.objects.create(name='Exemple 1', autor=self.user, )
        self.question = Question.objects.create(name='Question 1', test=self.test, autor=self.user, )
        self.answer = Answer.objects.create(name='Answer 1', question=self.question, is_correct=True, autor=self.user, )

    def test_answer_create(self):
        """ Тест создания ответа"""
        url = reverse('users_tests:answers-list')
        data = {
            'name': 'Answer 2',
            'question': self.question.id,
            'autor': self.user.id
        }
        response = self.client.post(url, data=data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Answer.objects.all().count(), 2
        )

    def test_answer_retrieve(self):
        """ Тест просмотра ответа"""
        url = reverse('users_tests:answers-detail', args=(self.answer.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.answer.name
        )

    def test_answer_list(self):
        """ Тест просмотра списка ответов"""
        url = reverse('users_tests:answers-list')
        response = self.client.get(url)
        result = [
            {
                'id': self.answer.id,
                'name': self.answer.name,
                'image': None,
                'is_correct': True,
                'question': self.question.pk,
                'autor': self.user.id
            }
        ]
        data = response.json()
        #print(data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_answer_update(self):
        """ Тест изменения ответа"""
        url = reverse('users_tests:answers-detail', args=(self.answer.pk,))
        data = {
            'name': 'Answer',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Answer'
        )

    def test_answer_delete(self):
        """ Тест удаления ответа"""
        url = reverse('users_tests:answers-detail', args=(self.answer.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Answer.objects.all().count(), 0
        )

class TestSessionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='student@gmail.com')
        self.client.force_authenticate(user=self.user)
        self.test = Test.objects.create(name='Exemple 1', autor=self.user, )
        self.question = Question.objects.create(name='Question 1', test=self.test, autor=self.user, )
        self.answer1 = Answer.objects.create(name='Answer 1', question=self.question, is_correct=True,
                                             autor=self.user, )
        self.answer2 = Answer.objects.create(name='Answer 2', question=self.question, autor=self.user, )

    def test_test_session_update(self):
        """ Тест ответа пользователя на вопрос"""
        url = reverse('users_tests:test_session')
        data = {
            'question': self.question.id,
            'user_answer': 'Answer 1'
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.data, {"message": 'Ответ верный'}
        )