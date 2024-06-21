from django.urls import path

from authapp.views import *
# from api.views import *
urlpatterns = [ path('Teamlead/', TeamLeadListCreate.as_view(), name="team-lead"),
               path('staff/', StaffListCreate.as_view(), name="staff"),
               path('frontoffice/', FrontOfficeListCreate.as_view(), name="frontoffice"), 
               path('hr/', HRListCreate.as_view(), name="hr"), 
            

               path('hrlogin/',Login.as_view(), name="hrlogin"),
    path('teamleadlogin/',LoginTeamlead.as_view(), name="teamleadlogin"),
    path('stafflogin/',LoginStaff.as_view(), name="stafflogin"),
    path('frontofficelogin/',LoginFrontoffice.as_view(), name="frontofficelogin"),
    # path('internlogin/',LoginIntern.as_view(), name="internlogin"),
    path('intern-reg/',InternCreateView.as_view(), name="inter-reg"),
    path('intern-login/',InternLoginView.as_view(), name='intern-login')
]

