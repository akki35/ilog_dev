from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^follow/$', 'myuserprofile.views.follow', name='follow'),
                       url(r'^unfollow/$', 'myuserprofile.views.unfollow', name='unfollow'),
                       url(r'^block/$', 'myuserprofile.views.block', name='block'),
                       url(r'^unblock/$', 'myuserprofile.views.unblock', name='unblock'),
)
