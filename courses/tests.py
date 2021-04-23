from .models import Course

import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ModelTests(TestCase):
    def setUp(self):
        self.old_count_courses = Course.objects.count()
        self.course = Course(
            title='HTML',
            date_start=datetime.date(2021, 5, 5),
            date_end=datetime.date(2021, 5, 14),
            count_lectures=20
        )
        self.course.save()

    def test_model_create_course(self):
        new_count = Course.objects.count()
        self.assertNotEqual(self.old_count_courses, new_count)

    def test_model_update_course(self):
        old_title = self.course.title
        self.course.title = 'CSS'
        self.course.save()
        new_title = self.course.title
        self.assertNotEqual(old_title, new_title)

    def test_model_delete_course(self):
        self.course.delete()
        self.course.save()
        new_count = Course.objects.count()
        self.assertNotEqual(self.old_count_courses, new_count)


class CourseAPITests(APITestCase):

    def setUp(self):
        self.list_url = reverse('courses_list')
        new_course = {
            "title": "HTML",
            "date_start": datetime.date(2021, 5, 5),
            'date_end': datetime.date(2021, 5, 14),
            'count_lectures': 20
        }
        self.response = self.client.post(self.list_url, new_course)

    def test_api_create_course(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_api_get_list_courses(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_get_course_by_id(self):
        url = reverse('course_by_id', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_get_course_by_title(self):
        url = reverse('course_by_title', kwargs={'title': 'HTML'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_update_course(self):
        change_course = {
            'title': 'CSS'
        }
        url = reverse('course_by_id', kwargs={'pk': 1})
        response = self.client.put(url, change_course, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_delete_course(self):
        url = reverse('course_by_id', kwargs={'pk': 1})
        response = self.client.delete(url, format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
