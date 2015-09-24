from rest_framework.test import APITestCase
from rest_framework import status

from django.core.urlresolvers import reverse

from .models import Location


class TestLocationCRUD(APITestCase):

    location_data = {
        'title': 'Whiteboard',
        'summary': 'A big big big board',
        'impact': 'How this makes an impact on Vokal Projects',
        'image_url': 'http://www.vokal.io/sites/default/files/sweet-pic.png'
    }

    location_put = {
        'title': 'Library',
        'summary': 'another summary',
        'imapct': 'Huge Impact',
        'image_url': 'http://www.vokal.io/sites/default/files/sweet-pic1.png'
    }

    def setUp(self):
        self.location = Location(title='Chalk Room',
                                 summary='This is a summary',
                                 impact='We do business here',
                                 image_url='http://www.vokal.io/sites/default/files/nice-pic.png')
        self.location.save()

        self.url_location_list = reverse('location_list_create')
        self.url_location_detail = reverse('retrieve_update_destroy_location',
                                           kwargs={'pk': self.location.id})

    def test_location_creation(self):
        response = self.client.post(self.url_location_list, self.location_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.location_data['title'])
        self.assertEqual(response.data['summary'], self.location_data['summary'])
        self.assertEqual(response.data['impact'], self.location_data['impact'])
        self.assertEqual(response.data['image_url'], self.location_data['image_url'])

    def test_location_list(self):
        response = self.client.get(self.url_location_list, {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], self.location.title)

    def test_location_put(self):
        response = self.client.put(self.url_location_detail, self.location_put)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_location_patch(self):
        response = self.client.patch(self.url_location_detail, {'title': 'NewRoom'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_location_get(self):
        response = self.client.get(self.url_location_detail, {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.location.title)
        self.assertEqual(response.data['summary'], self.location.summary)
        self.assertEqual(response.data['impact'], self.location.impact)
        self.assertEqual(response.data['image_url'], self.location.image_url)

    def test_duplicate_title_creation(self):
        response = self.client.post(self.url_location_list,
                                    {'title': self.location.title,
                                     'summary': 'anything',
                                     'impact': 'anything is impactful',
                                     'image_url': self.location.image_url})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_title_put(self):
        response = self.client.post(self.url_location_list, self.location_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.put(self.url_location_detail,
                                   {'title': self.location_data['title'],
                                    'summary': 'anything',
                                    'impact': 'anything is impactful',
                                    'image_url': self.location.image_url})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
