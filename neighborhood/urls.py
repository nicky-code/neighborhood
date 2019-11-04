from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^neighborhood/(?P<neighborhood_id>\d+)',views.neighborhood,name = 'neighborhood'),
     url(r'^profile/',views.new_profile,name = 'myProfile'),
    url(r'^new/profile$', views.new_profile,name='profile'),
     url(r'^newbusiness/',views.new_business,name = 'new-business'),
]