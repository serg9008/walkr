from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()        
    creator = models.ForeignKey(User)

class Photo(models.Model):
    url = models.URLField()
    lat = models.FloatField()
    lon = models.FloatField()    
    uploaded_by = models.ForeignKey(User)

# Provides a mapping between a Stop and its Photos
class PhotosPerStop(models.Model):
    stop = models.ForeignKey(Stop)
    photo = models.ForeignKey(Photo)

class Route(models.Model):
    creator = models.ForeignKey(User)

# Provides a mapping between a Route and its stops
class StopsPerRoute(models.Model):
    route = models.ForeignKey(Route)
    stop = models.ForeignKey(Stop)
    routePosition = models.IntegerField()

