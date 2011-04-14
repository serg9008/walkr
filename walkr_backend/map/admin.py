from django.contrib import admin
from walkr_backend.map.models import Stop, Route, Photo, PhotosPerStop, StopsPerRoute

admin.site.register(Stop)
admin.site.register(Route)
admin.site.register(Photo)
admin.site.register(PhotosPerStop)
admin.site.register(StopsPerRoute)
