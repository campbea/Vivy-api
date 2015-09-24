from django.do import IntegrityError

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from locations.models import Location
from locations.serializers import LocationSerializer, LocationPostSerializer


class LocationList(generics.ListCreateAPIView):

    # RFC should be admin only?
    permission_classes = (AllowAny)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def create(self, request):
        serializer = LocationPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        location = Location(**serializer.validated_data)

        try:
            location.save()
            result = LocationSerializer(location)
            return Response(result.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'detail': 'location already exists'},
                            status=status.HTTP_409_CONFLICT)


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (AllowAny)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
