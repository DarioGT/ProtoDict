from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
import globale.admin
globale.admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'modelibra.views.home', name='home'),
    # url(r'^modelibra/', include('modelibra.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('globale.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(globale.admin.site.urls)) ,

)
