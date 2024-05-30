from django.urls import path

from authapp.views import *
# from api.views import *
urlpatterns = [ path('team-lead/', TeamLeadListCreate.as_view(), name="team-lead"),
               path('staff/', StaffListCreate.as_view(), name="staff"),
               path('frontoffice/', FrontOfficeListCreate.as_view(), name="frontoffice"), 
               path('hr/', HRListCreate.as_view(), name="hr"), 
               path('intern/', InternListCreate.as_view(), name="intern"), 

               path('hrlogin/',Login.as_view(), name="hrlogin"),
    path('teamleadlogin/',LoginTeamlead.as_view(), name="teamleadlogin"),
    path('stafflogin/',LoginStaff.as_view(), name="stafflogin"),
    path('frontofficelogin/',LoginFrontoffice.as_view(), name="frontofficelogin"),
    path('internlogin/',LoginIntern.as_view(), name="internlogin"),
]

