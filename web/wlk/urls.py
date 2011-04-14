from django.conf.urls.defaults import *
from django.contrib import admin
#from django.contrib.gis import admin
import settings



admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wlk/', include('wlk.foo.urls')),
    # (r'', include('waypoints.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),

)
