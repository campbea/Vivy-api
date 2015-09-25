from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class ProjectTestMixin(object):

    def setUp(self):
        self.list_create_url = reverse('project_list_create')
        self.retrieve_update_destroy_url = lambda pk: reverse(
            'retrieve_update_destroy_project', args=[pk])


class ProjectTests(ProjectTestMixin, APITestCase):
    # Five test employees are loaded into test database
    fixtures = ['project_data.json']

    def test_list_project(self):
        url = reverse('project_list_create')
        url2 = self.retrieve_update_destroy_url(pk=1)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)
        response = self.client.get(url2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
