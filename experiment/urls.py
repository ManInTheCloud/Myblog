from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^home/',views.home,name='home'),
    url(r'^set_color/',views.set_color,name='set_color'),
    url(r'^show_color/',views.show_color,name='show_color'),
]