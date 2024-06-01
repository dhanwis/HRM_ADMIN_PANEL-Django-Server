from django.urls import path

from authapp.views import *
# from api.views import *
urlpatterns = [ path('team-lead/', TeamLeadListCreate.as_view(), name="team-lead"),
               path('staff/', StaffListCreate.as_view(), name="staff"),
               path('frontoffice/', FrontOfficeListCreate.as_view(), name="frontoffice"), 
               path('hr/', HRListCreate.as_view(), name="hr"), 
               path('intern/', InternListCreate.as_view(), name="intern"), 
               path('hrlogin/',HRLogin.as_view(),name="hr-login"),
               path('stafflogin/',StaffLogin.as_view(),name="staff-login"),
               path('teamleadlogin/',TeamLeadLogin.as_view(),name="teamlead-login"),
               path('frontofficelogin/',FrontOfficeLogin.as_view(),name="frontoffice-login")



]

