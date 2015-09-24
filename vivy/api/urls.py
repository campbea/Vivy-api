from django.conf.urls import patterns, url

from .employees_api import ListCreateEmployee, RetrieveUpdateDestroyEmployee


urlpatterns = patterns('',
    # Employee routes
    url(r'^v1/employee/$', ListCreateEmployee.as_view(), name='employee_list_create'),
    url(r'^v1/employee/(?P<pk>\d+)/$', RetrieveUpdateDestroyEmployee.as_view(), name='retrieve_update_destroy_employee'),
)
