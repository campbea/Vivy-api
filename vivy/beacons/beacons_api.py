from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from beacons.models import Beacon
from beacons.serializers import BeaconSerializer, BeaconPostSerializer


class BeaconList(generics.ListCreateAPIView):

    permission_classes = (AllowAny)
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer

    # try create without overriding create method
    # def create(self, request):
    #     serializer = BeaconPostSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     beacon = Beacon(**serializer.validated_data)
    #
    #     try:
    #         beacon.save()
    #         result = BeaconSerializer(beacon)
    #         return Response(result.data, )
