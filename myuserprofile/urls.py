from django.conf.urls import patterns, url
# from django.core.urlresolvers import reverse
from myuserprofile import views

urlpatterns = patterns('',
    url(r'^follow/$', views.follow, name='follow'),
    url(r'^unfollow/$', views.unfollow, name='unfollow'),
    url(r'^block/$', views.block, name='block'),
    url(r'^unblock/$', views.unblock, name='unblock'),
)


