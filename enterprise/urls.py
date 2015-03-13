from django.conf.urls import patterns, url
# from django.core.urlresolvers import reverse
from enterprise import views

urlpatterns = patterns('',
                       url(r'^register/$', views.register,),
                       # url(r'^login/$', views.login),
                       url(r'^(?P<slug>[^/]+)/$', 'enterprise_profile.views.enterprise_profile', name='enterprise_profile'),
                       url(r'^products/add_product/$', 'enterprise.views.add_product', name='add_product'),
                       url(r'^(?P<slug>[^/]+)/products/$', 'enterprise.views.product', name='product'),
                       # url(r'^logout/$', views.logout,)
)


# urlpatterns += patterns('django.contrib.auth.views',
#         url(r'^login/$', 'login', { 'template_name': 'registration/login.html'}, name='login' ),
#         url(r'^logout/$', 'logout', { 'template_name': 'registration/my_account.html', 'next_page':reverse('index') }, name='logout' ),
# )