from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples: url(r'^$', 'ilog_dev.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^#/$', 'nodes.views.like', name='like'),
                       url(r'^accounts/', include('accounts.urls'),),
                       url(r'^signup/$', 'accounts.views.signup', name='signup'),
                       url(r'^enterprise/', include('enterprise.urls', namespace='enterprise')),
                       url(r'^$', 'myuserprofile.views.home', name='home'),
                       url(r'^nodes/', include('nodes.urls', namespace='nodes')),
                       url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'accounts/cover.html'},
                           name='login'),
                       url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': 'login/'}, name='logout'),
                       url(r'^network/$', 'myuserprofile.views.network', name='network'),
                       url(r'^profile_edit/$', 'myuserprofile.views.profile_edit', name='profile_edit'),
                       url(r'^enterprise_profile_edit/$', 'enterprise_profile.views.enterprise_profile_edit',
                           name='enterprise_profile_edit'),
                       # url(r'^(?P<slug>[^/]+)/$', 'myuserprofile.views.profile', name='profile'),
                       url(r'^user/', include('myuserprofile.urls', namespace='myuserprofile')),
                       # url(r'^(?P<slug>[^/]+)/$', 'enterprise_profile.views.enterprise_profile', name='enterprise_profile'),
                       url(r'^search/$', 'search.views.search', name='search'),
                       # url(r'^', include('enterprise.urls'),),
                       url(r'^relationships', include('relationships.urls', namespace='relationships')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)