from django.urls import path
from .views import *
# from api.views import *
urlpatterns = [
    path('teamleadassign/',TeamLeadAssignCreate.as_view(),name='Teamleadassign'),
    path('teamleadupdate/<int:teamlead_id>',TeamLeadAssignUpdate.as_view(),name='Teamleadupdate'),
    path('teamleadassign/<int:teamlead_id>',TeamLeadAssignDelete.as_view(),name='Teamleaddelete'),
    path('studentassign/',StudentAssignlistCreate.as_view(),name='StudentAssignlistCreate'),
    path('studentassigndelete/<int:student_id>/',StudentAssignDelete.as_view(),name="studenttaskdelete"),
    path('projectassign/',AssignProjectCreate.as_view(),name='projectassign'),
    path('leaverequest/', LeaveLetterCreate.as_view(), name='submit_leave_request'),
    
# path('leave-request/<int:request_id>/', process_leave_request, name='process_leave_request'),


]


