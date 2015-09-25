from django.db import IntegrityError

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from beacons.models import Beacon
from beacons.serializers import BeaconSerializer, BeaconPostPutSerializer


class ListCreateBeacon(generics.ListCreateAPIView):

    permission_classes = (AllowAny,)
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer

    def create(self, request):
        serializer = BeaconPostPutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        beacon = Beacon(**serializer.validated_data)

        beacon.save()
        result = BeaconSerializer(beacon)
        return Response(result.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyBeacon(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BeaconSerializer
    lookup_field = 'beacon_uuid'

    def get_queryset(self):
        uuid = self.kwargs['beacon_uuid']
        return Beacon.objects.filter(beacon_uuid=uuid)

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return BeaconPostPutSerializer
        return BeaconSerializer
