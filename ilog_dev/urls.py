from django.conf.urls import patterns, include, url
from django.contrib import admin
# from ilog_dev import accounts

urlpatterns = patterns('',
                       # Examples: url(r'^$', 'ilog_dev.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('accounts.urls'),),
                       url(r'^enterprise/', include('enterprise.urls'),),
                       url(r'^$', 'myuserprofile.views.home', name='home'),
                       url(r'^nodes/', include('nodes.urls')),
                       url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'accounts/cover.html'},
                           name='login'),
                       url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
                       url(r'^network/$', 'myuserprofile.views.network', name='network'),
                       url(r'^profile_edit/$', 'myuserprofile.views.profile_edit', name='profile_edit'),
                       url(r'^enterprise_profile_edit/$', 'enterprise_profile.views.enterprise_profile_edit',
                           name='enterprise_profile_edit'),
                       url(r'^(?P<slug>[^/]+)/$', 'myuserprofile.views.profile', name='profile'),
)
