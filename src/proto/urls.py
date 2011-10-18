from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
import globale.admin
globale.admin.autodiscover()

from proto.metaDb.views import protoGridDefinition  


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'modelibra.views.home', name='home'),
    # url(r'^modelibra/', include('modelibra.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('globale.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/protoExtjsGridDefinition/?$', protoGridDefinition ),
    url(r'^admin/', include(globale.admin.site.urls)) ,


#    (r'^apps/(?P<app>[^/]+)/(?P<view>[^/]+)/?(?P<path>.+)?$', 'core.appdispatcher.dispatch' ),
#    (r'^apps/(?P<app>[^/]+)/?$', 'core.appdispatcher.dispatch' ),
)

