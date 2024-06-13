from django.urls import path
from .views import *
# from api.views import *
urlpatterns = [ path('teamleadassign/',TeamLeadAssignCreate.as_view(),name='Teamleadassign'),
               path("teamleadupdate/<int:teamlead_id>",TeamLeadAssignUpdate.as_view(),name="teamleadassignupdate"),
               path("teamleaddelete/<int:teamlead_id>",TeamLeadAssignDelete.as_view(),name="teamleaddelete"),
               path('studentassign/listcreate/',StudentAssignlistCreate.as_view(),name='studentassignlistcreateview'),
               
               
               path('projectassign/listcreate/',ProjectAssignlistCreate.as_view(),name='staffassignlistcreateview'),
               path("projectdelete/<int:project_id>",ProjectAssignDelete.as_view(),name="projectdelete"),
               path("projectupdate/<int:project_id>/",projectAssignUpdate.as_view(),name="projectassignupdate"),
               
               
               path("studentdelete/<int:student_id>",StudentAssignDelete.as_view(),name="studentdelete"),
               path("studentupdate/<int:student_id>",StudentAssignUpdate.as_view(),name='studentassignupdate'),
               
               
               path('digitaltable/create',DigitalTableCreate.as_view(),name='digitaltablecreate'),
               path('digitaltableupdate/<int:digital_id>',DigitalTableUpdate.as_view(),name='digitaltableupdate'),
               path('digitaltabledelete/<int:digital_id>',DigitalTableDelete.as_view(),name='digitaltabledelete'),
               
               
               path('teamtablecreate',TeamTableCreate.as_view(),name='teamtablecreate'),
               path('teamtabledelete/<int:team_id>',TeamTableDelete.as_view(),name='teamtabledelete;'),
               
               
               path('leavecreate',LeaveCreate.as_view(),name='leavecreate'),
]


