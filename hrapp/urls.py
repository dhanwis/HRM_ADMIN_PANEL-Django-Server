from django.urls import path
from .views import *
# from api.views import *
urlpatterns = [ path('teamleadassign/',TeamLeadAssignCreate.as_view(),name='Teamleadassign'),
               path("teamleadupdate/<int:teamlead_id>/",TeamLeadAssignUpdate.as_view(),name="teamleadassignupdate"),
               path("teamleaddelete/<int:teamlead_id>",TeamLeadDelete.as_view(),name="teamleaddelete"),
            #    path("projectassign/",ProjectAssignCreate.as_view(),name="projectassign")


]


