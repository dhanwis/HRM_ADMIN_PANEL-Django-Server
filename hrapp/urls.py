from django.urls import path
from .views import *
# from api.views import *
urlpatterns = [ path('teamleadassign/',TeamLeadAssignCreate.as_view(),name='Teamleadassign'),
               path("teamleadupdate/<int:teamlead_id>/",TeamLeadAssignUpdate.as_view(),name="teamleadassignupdate")

]

