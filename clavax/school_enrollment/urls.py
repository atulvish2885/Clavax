from django.urls import path
#from clavax.views import *
from . import views
from django.conf.urls import url
#from . views import Studentlist





urlpatterns = [
    path('home/',views.homepage,name="homepage"),
    url(r'^renderpage/', views.renderpage, name = 'render'),
    path('studentlist/',StudentList.as_view(),name='student list'),


]
