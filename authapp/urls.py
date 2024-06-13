from django.urls import path

from authapp.views import *
# from api.views import *
urlpatterns = [ path('Teamlead/', TeamLeadListCreate.as_view(), name="team-lead"),
               path('staff/', StaffListCreate.as_view(), name="staff"),
               path('frontoffice/', FrontOfficeListCreate.as_view(), name="frontoffice"), 
               path('hr/', HRListCreate.as_view(), name="hr"), 
               path('intern/', InternListCreate.as_view(), name="intern"), 
               path('hrlogin/',Login.as_view(),name='hrlogin'),
               path('teamlogin/',TeamLogin.as_view(),name="teamLogin"),
               path('stafflogin/',StaffLogin.as_view(),name="stafflogin"),
               path('frontlogin/',FrontLogin.as_view(),name="frontlogin"),
               path('internlogin/',InternLogin.as_view(),name="internlogin")
               
]

