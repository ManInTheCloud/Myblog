from django.contrib.auth.views import login,logout
from django.conf.urls import include,url

urlpatterns=[
    url(r'^login/$',login),
    url(r'^logout/$',logout),
]