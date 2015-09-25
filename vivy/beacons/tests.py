from rest_framework import status

from django.core.urlresolvers import reverse

from .models import Beacon

from locations.models import Location
from locations.tests import (TestLocationCRUD)


class TestBeaconCRUD(TestLocationCRUD):

    def setUp(self):
        super(TestBeaconCRUD, self).setUp()

        self.beacon_data = {
            'beacon_uuid': '96C87DF2DE794436A189F86FD6C21F3A',
            'location': self.new_location.id
        }

        self.beacon = Beacon(beacon_uuid='9B09107EE3794C21A0641290D39F72A4',
                             location=self.location)
        self.beacon.save()

        self.url_beacon_list = reverse('beacon_list_create')
        self.url_beacon_detail = reverse('retreive_update_destroy_beacon',
                                         kwargs={'beacon_uuid': self.beacon.beacon_uuid})

    def test_beacon_creation(self):
        response = self.client.post(self.url_beacon_list, self.beacon_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_beacon_creation_400(self):
        response = self.client.post(self.url_beacon_list,
                                    {'beacon_uuid': '12fs',
                                     'location': self.new_location.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.post(self.url_beacon_list,
                                    {'beacon_uuid': self.beacon_data['beacon_uuid'],
                                     'location': 100})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_beacon_get_list(self):
        response = self.client.get(self.url_beacon_list, {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_beacon_get_detail(self):
        response = self.client.get(self.url_beacon_detail, {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_beacon_patch(self):
        response = self.client.patch(self.url_beacon_detail, {'location': self.new_location.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_id = Location.objects.get(title=self.new_location.title).id
        self.assertEqual(response.data['location'], new_id)

    def test_beacon_delete(self):
        response = self.client.delete(self.url_beacon_detail, {})
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
