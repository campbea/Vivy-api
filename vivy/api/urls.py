from django.conf.urls import patterns, url

from .employees_api import ListCreateEmployee, RetrieveUpdateDestroyEmployee
from .projects_api import ListCreateProject, RetrieveUpdateDestroyProject
from .locations_api import ListCreateLocation, RetrieveUpdateDestroyLocation
from .beacons_api import ListCreateBeacon, RetrieveUpdateDestroyBeacon

urlpatterns = patterns(
    '',
    # Project Routes
    url(r'^project/?$', ListCreateProject.as_view(), name='project_list_create'),
    url(r'^project/(?P<pk>\d+)/?$', RetrieveUpdateDestroyProject.as_view(),
        name='retrieve_update_destroy_project'),
    # Employee routes
    url(r'^employee/?$', ListCreateEmployee.as_view(), name='employee_list_create'),
    url(r'^employee/(?P<pk>\d+)/?$', RetrieveUpdateDestroyEmployee.as_view(),
        name='retrieve_update_destroy_employee'),
    # Location Routes
    url(r'^location/?$', ListCreateLocation.as_view(), name='location_list_create'),
    url(r'^location/(?P<pk>\d+)/?$', RetrieveUpdateDestroyLocation.as_view(),
        name='retrieve_update_destroy_location'),
    # Beacon Routes
    url(r'^beacons/?$', ListCreateBeacon.as_view(), name='beacon_list_create'),
    url(r'^beacons/(?P<beacon_uuid>[A-Z0-9]{32})/?$', RetrieveUpdateDestroyBeacon.as_view(),
        name='retreive_update_destroy_beacon'),
    # Update Employees
    # url(r'^update-employees/?$', UpdateEmployees.as_view(), name='beacon_list_create'),
)
