from django.urls import path
from .views import *
# from api.views import *
urlpatterns = [
    path('teamleadassign/',TeamLeadAssignCreate.as_view(),name='Teamleadassign'),
    path('teamleadupdate/<int:teamlead_id>',TeamLeadAssignUpdate.as_view(),name='Teamleadupdate'),
    path('teamleadassign/<int:teamlead_id>',TeamLeadAssignDelete.as_view(),name='Teamleaddelete'),
    path('studentassign/',StudentAssignlistCreate.as_view(),name='StudentAssignlistCreate'),
    path('studentassign/<int:pk>/update-status/',StudentStatusUpdateView.as_view(),name='update_studentassign_status'),
    path('studentassigndelete/<int:student_id>/',StudentAssignDelete.as_view(),name="studenttaskdelete"),
    path('projectassign/',AssignProjectCreate.as_view(),name='projectassign'),
    path('projectassign/<int:pk>/update-status/',AssignProjectStatusUpdate.as_view(),name='update_projectassign_status'),
    path('leaverequest/', LeaveLetterCreate.as_view(), name='submit_leave_request'),
    path('leave/list/', LeaveListView.as_view(), name='leave-list'),
    path('leave/update/<int:pk>/', LeaveUpdateView.as_view(), name='leave-update'),
    path('staff/noteshare/',NotesSharinglistCreate.as_view(),name="notesharingto intern"),
    path('staff/statusshare/',StatusSharinglistCreate.as_view(),name="statussharetoteamlead"),
    path('teamlead/digitalmarketcreate/',DigitalTableCreate.as_view(),name="digitalmarketcreate"),
    path('teamlead/digitalmarketupdate/<int:digital_id>',DigitalTableUpdate.as_view(),name="digitalmarketupdate"),
    path('teamlead/digitalmarketdelete/<int:digital_id>',DigitalTableDelete.as_view(),name="digitalmarketupdate"),
    path('hr/jobapply/',JobApplyCreate.as_view(),name='hrjobalert'),

]


