from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, AllowAny

from employees.models import Employee
from employees.serializers import EmployeeSerializer


# We can use this later for authentication
class AllowGetOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method is 'GET':
            return True

        return request.user.is_staff


class ListCreateEmployee(generics.ListCreateAPIView):

    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny, )


class RetrieveUpdateDestroyEmployee(generics.RetrieveUpdateDestroyAPIView):

    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny, )
