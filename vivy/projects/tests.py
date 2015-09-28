from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class ProjectTestMixin(object):

    def setUp(self):
        self.list_create_url = reverse('project_list_create')
        self.retrieve_update_destroy_url = lambda pk: reverse(
            'retrieve_update_destroy_project', args=[pk])

        self.data = {
            "name": "Vivy",
            "headline": "Showing shit off to clients",
            "logo_url": "http://fakeurl.com/images/logo.png",
            "opportunity": "Get more clients",
            "solution": "Vivy",
            "technology": "iOS - Ipad application",
            "staff": [1],
            "screenshot" : []
        }

class ProjectTests(ProjectTestMixin, APITestCase):
    # Five test employees are loaded into test database
    # Four projects are loaded into test database
    fixtures = ['project_data.json', 'employee_data.json']

    def test_create_project(self):
        url = self.list_create_url
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['name'], self.data['name'])
        self.assertEqual(response.data['headline'], self.data['headline'])
        self.assertEqual(response.data['opportunity'], self.data['opportunity'])
        self.assertEqual(response.data['solution'], self.data['solution'])
        self.assertEqual(response.data['technology'], self.data['technology'])
        self.assertEqual(response.data['staff'], self.data['staff'])

    def test_create_duplicate_project_fail(self):
        url = self.list_create_url
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['id'])

        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_project(self):
        url = reverse('project_list_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 4)

    def test_get_project_detail(self):
        url = self.retrieve_update_destroy_url(pk=1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['name'], 'Grainger')
        self.assertEqual(response.data['staff'], [1])

    def test_update_project(self):
        url = self.retrieve_update_destroy_url(pk=1)
        response = self.client.patch(url, {"name":"GALANTIS"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['id'])
        self.assertEqual(response.data['name'], 'GALANTIS')

    def test_delete_project(self):
        url = self.retrieve_update_destroy_url(pk=1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
