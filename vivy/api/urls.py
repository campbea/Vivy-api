from django.conf.urls import patterns, url

from .employees_api import ListCreateEmployee, RetrieveUpdateDestroyEmployee
from .projects_api import ListCreateProject, RetrieveUpdateDestroyProject
from .locations_api import ListCreateLocation, RetrieveUpdateDestroyLocation

urlpatterns = patterns(
    # Project Routes
    url(r'^v1/project/$', ListCreateProject.as_view(), name='project_list_create'),
    url(r'^v1/project/(?P<pk>\d+)/$', RetrieveUpdateDestroyProject.as_view(),
        name='retrieve_update_destroy_project'),
    # Employee routes
    url(r'^v1/employee/$', ListCreateEmployee.as_view(), name='employee_list_create'),
    url(r'^v1/employee/(?P<pk>\d+)/$', RetrieveUpdateDestroyEmployee.as_view(),
        name='retrieve_update_destroy_employee'),
    # Location Routes
    url(r'^v1/location/$', ListCreateLocation.as_view(), name='location_list_create'),
    url(r'^v1/location/(?P<pk>\d+)/$', RetrieveUpdateDestroyLocation.as_view(),
        name='retrieve_update_destroy_location'),

)
