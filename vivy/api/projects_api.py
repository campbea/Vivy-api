from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, AllowAny

from projects.models import Project
from projects.serializers import ProjectSerializer


# We can use this later for authentication
class AllowGetOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method is 'GET':
            return True

        return request.user.is_staff


class ListCreateProject(generics.ListCreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )


class RetrieveUpdateDestroyProject(generics.RetrieveUpdateDestroyAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (AllowAny, )
