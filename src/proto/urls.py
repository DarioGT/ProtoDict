from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
import globale.admin
globale.admin.autodiscover()

from proto.metaDb.views import protoGridDefinition  


urlpatterns = patterns('',

    url(r'^admin/protoExtjsGridDefinition/?$', protoGridDefinition ),
    url(r'^admin/', include(globale.admin.site.urls)) ,

    url(r'^protoExt$', direct_to_template, { 'template': 'protoExt.html' }),
    url(r'^protoExt/', include('protoExt.urls')),

    url(r'^prueba1$', direct_to_template, { 'template': 'prueba.html' }),
    url(r'^prueba2$', direct_to_template, { 'template': 'prueba.html' }),

)


#    (r'^apps/(?P<app>[^/]+)/(?P<view>[^/]+)/?(?P<path>.+)?$', 'core.appdispatcher.dispatch' ),
#    (r'^apps/(?P<app>[^/]+)/?$', 'core.appdispatcher.dispatch' ),
