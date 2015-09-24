from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from beacons.models import Beacon
from beacons.serializers import BeaconSerializer, BeaconPostSerializer


class ListCreateBeacon(generics.ListCreateAPIView):

    permission_classes = (AllowAny,)
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer


class RetrieveUpdateDestroyBeacon(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BeaconSerializer
    lookup_field = 'beacon_uuid'

    def get_queryset(self):
        uuid = self.kwargs['beacon_uuid']
        return Beacon.objects.filter(beacon_uuid=uuid)
