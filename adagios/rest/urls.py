from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    #(r'/(?P<format>.+)/addhost/(?P<host_name>.+)/(?P<ip>.+)/(?P<group_name>.+)/?$', 'okconfig.views.addhost'),
    #(r'/(?P<format>.+)/get_templates/?$', 'okconfig.views.get_templates'),
    #(r'/(?P<format>.+)/get_templates/(?P<test_field>.+)?$', 'okconfig.views.get_templates'),
    #(r'/call_function/(?P<format>.+)//(?P<test_field>.+)?$', 'okconfig.views.get_templates'),
    #(r'/(?P<format>.+)/(?P<attribute>.+)/?$', 'okconfig.views.get'),
    (r'/$', 'rest.views.index'),
    (r'/(?P<format>.+)/(?P<attribute>.+)/?$', 'rest.views.handle_request'),    

    #(r'/contact/(?P<contact_name>.+)$', 'objectbrowser.views.get_contact'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)