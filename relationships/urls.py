from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # url(r'^follow/$', views.follow, name='follow'),
                       # url(r'^unfollow/$', views.unfollow, name='unfollow'),
                       # url(r'^block/$', views.block, name='block'),
                       # url(r'^unblock/$', views.unblock, name='unblock'),
                       url(r'^(?P<slug>[^/]+)/$', 'myuserprofile.views.profile', name='profile'),
                       url(r'^/follow/$', 'myuserprofile.views.follow', name='follow'),
                       url(r'^(?P<slug>[^/]+)/unfollow/$', 'myuserprofile.views.unfollow', name='unfollow'),
)
