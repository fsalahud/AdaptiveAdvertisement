from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^adduser/$', views.addUser, name='adduser'), 
    url(r'^showusers/$', views.showUsers, name='showusers'),
    url(r'^showanalyze1/$', views.analyze1, name='showanalyze1'),
    url(r'^showanalyze2/$', views.analyze2, name='showanalyze2'),
    url(r'^showaddress/$', views.address, name='showaddress'),
    url(r'^showcategorize1/$', views.categorize1, name='showcategorize1'),
    url(r'^showcategorize2/$', views.categorize2, name='showcategorize2'),
    url(r'^showdisplay1/$', views.display1, name='showdisplay1'),
    url(r'^showdisplay2/$', views.display2, name='showdisplay2'),
    url(r'^img/(?P<id>\d+)/$', views.getOne, name='getOne'),
    url(r'^img/$', views.getImage, name='getImage'),
    url(r'^exe/$', views.exe, name='exe'),
    url(r'^temporary/$', views.temporary, name='temporary'),
    # url(r'^showage/$', views.count_ages, name='count_ages'),
    url(r'^showdemographics/$', views.democount, name='democount'),

]