from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse
from myuserprofile import views

urlpatterns = patterns('',
                       # url(r'^follow/$', views.follow, name='follow'),
                       # url(r'^unfollow/$', views.unfollow, name='unfollow'),
                       # url(r'^block/$', views.block, name='block'),
                       # url(r'^unblock/$', views.unblock, name='unblock'),
                       url(r'^edit/$', 'myuserprofile.views.profile_edit', name='profile_edit'),
                       url(r'^network/$', 'myuserprofile.views.network', name='network'),
                       url(r'^skillset/$', 'myuserprofile.views.skillset', name='skillset'),
                       url(r'^relationships', include('relationships.urls', namespace='relationships')),
                       url(r'^(?P<slug>[^/]+)/$', 'myuserprofile.views.profile', name='profile'),
                       url(r'^(?P<slug>[^/]+)/$', 'myuserprofile.views.activity', name='activity'),



                       # url(r'^(?P<slug>[^/]+)/follow/$', 'myuserprofile.views.follow', name='follow'),
                       # url(r'^(?P<slug>[^/]+)/unfollow/$', 'myuserprofile.views.unfollow', name='unfollow'),
)


