from django.conf.urls import url
from . import views

urlpatterns=[
    #正则表达式语法（?P<name>pattern),name对应view函数中的形参名
    url(r'^home/',views.home,{'template_name':'test/test.html'},name='home'),
    url(r'^set_color/',views.set_color,name='set_color'),
    url(r'^show_color/',views.show_color,name='show_color'),

    url(r'^mydate/(?P<month>\w{3}/(?P<day>\d\d)\$',views.my_view),  #\d捕捉结果也是字符串
    url(r'^mydate/birthday/$',views.my_view,{"month":"Dec","day":"05"}),
    url(r'^somepage/$',views.method_splitter,{"GET":views.some_page_get,"POST":views.some_page_post}),
    url(r'^view1/$',views.requires_login(views.my_view)),
]