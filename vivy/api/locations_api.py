from rest_framework import generics
from rest_framework.permissions import AllowAny

from locations.models import Location
from locations.serializers import LocationSerializer


class ListCreateLocation(generics.ListCreateAPIView):

    permission_classes = (AllowAny,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class RetrieveUpdateDestroyLocation(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (AllowAny,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
