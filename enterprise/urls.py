from django.conf.urls import patterns, url
# from django.core.urlresolvers import reverse
from enterprise import views

urlpatterns = patterns('',
                       url(r'^register/$', views.register,),
                       # url(r'^login/$', views.login),
                       # url(r'^logout/$', views.logout,)
)


# urlpatterns += patterns('django.contrib.auth.views',
#         url(r'^login/$', 'login', { 'template_name': 'registration/login.html'}, name='login' ),
#         url(r'^logout/$', 'logout', { 'template_name': 'registration/my_account.html', 'next_page':reverse('index') }, name='logout' ),
# )