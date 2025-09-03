from .views import *
from django.urls import path


urlpatterns=[
    path('',index,name="index"),
    path('resume/',resume,name="resume"),
    path('contact/',contact,name="contact"),
    path('project/',project,name="project"),
     path("api/contact/", contact_api, name="contact_api"),


]