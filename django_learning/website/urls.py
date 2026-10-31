from django.urls import path
from website.views import *

urlpatterns = [
    path("",index_view),
    path("index",index_view),
    path("home",index_view),
]