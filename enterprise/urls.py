from django.conf.urls import patterns, url
# from django.core.urlresolvers import reverse
from enterprise import views

urlpatterns = patterns('',
                       url(r'^register/$', views.register,),

                       url(r'^add_product/$', 'enterprise.views.add_product', name='add_product'),
                       url(r'^edit/$', 'enterprise_profile.views.enterprise_profile_edit',
                           name='enterprise_profile_edit'),
                       url(r'^(?P<slug>[^/]+)/$', 'enterprise_profile.views.enterprise_profile',
                           name='enterprise_profile'),

                       url(r'^(?P<slug>[^/]+)/products/$', 'enterprise.views.product', name='product'),

)


# urlpatterns += patterns('django.contrib.auth.views',
#         url(r'^login/$', 'login', { 'template_name': 'registration/login.html'}, name='login' ),
#         url(r'^logout/$', 'logout', { 'template_name': 'registration/my_account.html', 'next_page':reverse('index') }, name='logout' ),
# )