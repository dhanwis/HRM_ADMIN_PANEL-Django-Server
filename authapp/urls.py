from django.urls import path

from authapp.views import *
# from api.views import *
urlpatterns = [ path('Teamlead/', TeamLeadListCreate.as_view(), name="team-lead"),
               path('Staff/', StaffListCreate.as_view(), name="staff"),
               path('Frontoffice/', FrontOfficeListCreate.as_view(), name="frontoffice"), 
               path('Hr/', HRListCreate.as_view(), name="hr"), 
        
    path('hrlogin/',Login.as_view(), name="hrlogin"),
    path('teamleadlogin/',LoginTeamlead.as_view(), name="teamleadlogin"),
    path('stafflogin/',LoginStaff.as_view(), name="stafflogin"),
    path('frontofficelogin/',LoginFrontoffice.as_view(), name="frontofficelogin"),
    # path('internlogin/',LoginIntern.as_view(), name="internlogin"),
    path('intern-reg/',InternCreateView.as_view(), name="inter-reg"),
    path('intern-login/',InternLoginView.as_view(), name='intern-login'),
    path('intern/reference/',ReferencelistCreate.as_view(),name="internreference"),
    path('intern/referencedelete/<int:reference_id>',ReferenceDelete.as_view(),name="internreferencedelete"),
    path('intern/feedback/',FeedbackListCreateView.as_view(),name="internfeedback"),
    path('intern/testimonal',TestimonialListCreateView.as_view(),name="interntestimonal"),
    path('users/',Allusers.as_view(),name="alluserexpecthr"),
    path('allusers/<int:pk>/', Allusers.as_view(), name='allusers-detail'),
    

]

