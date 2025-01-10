from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='super@gmail.com', is_staff=True, is_superuser=True,)
        self.course = Course.objects.create(name='Test course 1', description='Test course 1', autor=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_create(self):
        """ Тест создания курса"""
        url = reverse('courses:courses-list')
        data = {
            'name': 'Test course 2'
        }
        response = self.client.post(url, data=data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_retrieve(self):
        """ Тест просмотра курса"""
        url = reverse('courses:courses-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.course.name
        )

    def test_course_list(self):
        url = reverse('courses:courses-list')
        response = self.client.get(url)
        result = [
            {
            'id': self.course.id,
            'name': self.course.name,
            'description': self.course.description,
            'autor': self.user.id
            }
        ]
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_course_update(self):
        """ Тест изменения курса"""
        url = reverse('courses:courses-detail', args=(self.course.pk,))
        data = {
            'name': 'Test',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Test'
        )

    def test_course_delete(self):
        """ Тест удаления курса"""
        url = reverse('courses:courses-detail', args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='super@gmail.com', is_staff=True, is_superuser=True,)
        self.course = Course.objects.create(name='Test course 1', description='Test course 1', autor=self.user)
        self.lesson = Lesson.objects.create(name='Test lesson 1', lesson_content='Test lesson 1', course=self.course,
                                            autor=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        """ Тест создания урока"""
        url = reverse('courses:lessons_create')
        data = {
            'name': 'Test lesson 2',
            'lesson_content': 'Test lesson 2',
        }
        response = self.client.post(url, data=data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_retrieve(self):
        """ Тест просмотра урока"""
        url = reverse('courses:lessons_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    def test_lesson_list(self):
        url = reverse('courses:lessons_list')
        response = self.client.get(url)
        result = [
            {
                'autor': self.user.id,
                'course': self.course.id,
                'id': self.lesson.id,
                'image': None,
                'lesson_content': self.lesson.lesson_content,
                'name': self.lesson.name,
                'status': self.lesson.status,
                'video': None
            }
        ]

        data = response.json()
        # print(data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_lesson_update(self):
        """ Тест изменения урока"""
        url = reverse('courses:lessons_update', args=(self.lesson.pk,))
        data = {
            'name': 'Test 1',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Test 1'
        )

    def test_lesson_delete(self):
        """ Тест удаления курса"""
        url = reverse('courses:lessons_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )
