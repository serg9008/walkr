from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^walkr/$', 'walkr_backend.map.views.index'),
    (r'^walkr/savestop', 'walkr_backend.map.views.savestop'),
    (r'^walkr/saveroute', 'walkr_backend.map.views.saveroute'),
    (r'^walkr/map', 'walkr_backend.map.views.map'),
    (r'^walkr/index', 'walkr_backend.map.views.index'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
