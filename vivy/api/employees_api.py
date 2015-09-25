from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, AllowAny

from employees.models import Employee
from employees.serializers import EmployeeSerializer
from employees.utils import scrape_employee_page


# We can use this later for authentication
class AllowGetOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method is 'GET':
            return True

        return request.user.is_staff


class ListCreateEmployee(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny, )


class RetrieveUpdateDestroyEmployee(generics.RetrieveUpdateDestroyAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny, )


class UpdateEmployees(generics.CreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        if scrape_employee_page('https://www.vokal.io/team'):
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
