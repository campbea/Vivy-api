from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase

# from .utils import scrape_employee_page

class EmployeeTestMixin(object):

    def setUp(self):
        self.list_create_url = reverse('employee_list_create')
        self.retrieve_update_destroy_url = lambda pk: reverse(
            'retrieve_update_destroy_employee', args=[pk])

        self.data = {
            "first_name": "Loco",
            "last_name": "Pollo",
            "title": "BOSS",
            "image_url": "http://orig06.deviantart.net/8ac6/f/2010/214/1/f/crazy_chicken_by_dustclaw.gif",
            "summary": "one crazy chicken",
        }


class EmployeeTests(EmployeeTestMixin, APITestCase):
    # Five test employees are loaded into test database
    fixtures = ['employee_data.json']

    def test_create_employee(self):
        url = self.list_create_url
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['first_name'], self.data['first_name'])
        self.assertEqual(response.data['last_name'], self.data['last_name'])
        self.assertEqual(response.data['title'], self.data['title'])
        self.assertEqual(response.data['image_url'], self.data['image_url'])
        self.assertEqual(response.data['summary'], self.data['summary'])

    def test_create_same_employee_fail(self):
        url = self.list_create_url
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['id'])

        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_employees(self):
        url = self.list_create_url
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 5)

    def test_get_an_employee(self):
        url = self.retrieve_update_destroy_url(pk=1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jarrett')
        self.assertEqual(response.data['last_name'], 'Widman')

    def test_update_an_employee(self):
        url = self.retrieve_update_destroy_url(pk=1)
        response = self.client.patch(url, {"first_name":"MAJORLAZER"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'MAJORLAZER')

    def test_delete_an_employee(self):
        url = self.list_create_url
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        employee_pk = response.data['id']

        url = self.retrieve_update_destroy_url(pk=employee_pk)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def test_scrape_page(self):
    #     scrape_employee_page('https://www.vokal.io/team')
