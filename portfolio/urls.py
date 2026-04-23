from django.urls import path
from . import views


urlpatterns = [
    path("",views.home ,name="about"),
    path("Resume/",views.Resume ,name="Resume"),
    path("project/",views.Projects ,name="project"),
    path("contact/",views.contact ,name="contact"),
   
]