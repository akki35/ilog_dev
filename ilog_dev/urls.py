from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^$', 'myuserprofile.views.home', name='home'),
                       url(r'^signup/$', 'accounts.views.signup', name='signup'),
                       url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'accounts/cover.html'},
                           name='login'),
                       url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': 'login/'}, name='logout'),

                       url(r'^accounts/', include('accounts.urls'),),
                       url(r'^enterprise/', include('enterprise.urls', namespace='enterprise')),
                       url(r'^user/', include('myuserprofile.urls', namespace='myuserprofile')),
                       url(r'^nodes/', include('nodes.urls', namespace='nodes')),



                       url(r'^#/$', 'nodes.views.like', name='like'),
                       url(r'^search/$', 'search.views.search', name='search'),


)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += patterns('',
#                         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#                          'document_root': settings.MEDIA_ROOT}))


# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)