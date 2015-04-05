from django.conf.urls import patterns, url
# from django.core.urlresolvers import reverse
from enterprise import views


urlpatterns = patterns('',
                       url(r'^register/$', views.register,),

                       url(r'^add_product/$', 'enterprise.views.add_product', name='add_product'),
                       url(r'^add_asset/$', 'enterprise.views.add_asset', name='add_asset'),
                       url(r'^add_type/$', 'enterprise.views.add_type', name='add_type'),
                       url(r'^add_material/$', 'enterprise.views.add_material', name='add_material'),
                       url(r'^add_operation/$', 'enterprise.views.add_operation', name='add_operation'),
                       url(r'^edit/$', 'enterprise_profile.views.enterprise_profile_edit',
                           name='enterprise_profile_edit'),
                       url(r'^(?P<slug>[^/]+)/$', 'enterprise_profile.views.enterprise_profile',
                           name='enterprise_profile'),

                       url(r'^(?P<slug>[^/]+)/products/$', 'enterprise.views.product', name='product'),
                       url(r'^(?P<slug>[^/]+)/people/$', 'enterprise.views.people', name='people'),
                       url(r'^(?P<slug>[^/]+)/about/$', 'enterprise.views.about', name='about'),
                       url(r'^(?P<slug>[^/]+)/capability/$', 'enterprise.views.capability', name='capability'),

)


# urlpatterns += patterns('django.contrib.auth.views',
#         url(r'^login/$', 'login', { 'template_name': 'registration/login.html'}, name='login' ),
#         url(r'^logout/$', 'logout', { 'template_name': 'registration/my_account.html', 'next_page':reverse('index') }, name='logout' ),
# )