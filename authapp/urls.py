from django.urls import path

from authapp.views import TeamLeadListCreate
# from api.views import *
urlpatterns = [ path('team-lead/', TeamLeadListCreate.as_view(), name="team-lead")
    
]

