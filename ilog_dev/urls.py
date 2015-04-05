from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)), # admin interface

                       url(r'^$', 'myuserprofile.views.home', name='home'), # home page
                       url(r'^logup$', 'accounts.views.logup', name='logup'), # logup page
                       url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),  # login page, redirects to 'home'
                       url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': 'login'}, name='logout'), # logout page, redirects to 'login'

                       url(r'^accounts/', include('accounts.urls', namespace='accounts')), # no use for now
                       url(r'^enterprise/', include('enterprise.urls', namespace='enterprise')),  # enterprise domain
                       url(r'^user/', include('myuserprofile.urls', namespace='myuserprofile')), # user domain
                       url(r'^nodes/', include('nodes.urls', namespace='nodes')),


                       url(r'^like/$', 'nodes.views.like', name='like'),
                       url(r'^search/$', 'search.views.search', name='search'),
                       # url(r'^search_adv/$', 'search.views.search_adv', name='search_adv'),

                       url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       url(r'^notifications/$', 'activities.views.notifications', name='notifications'),

                       url(r'^robots.txt/$', TemplateView.as_view(template_name='robots.txt')),


)   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += patterns('',
#                         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#                          'document_root': settings.MEDIA_ROOT}))

# urlpatterns = patterns('',
# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)