from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.template import RequestContext
from walkr_backend.map.models import *
import json
import datetime

# LOGGING
import logging
LOG_FILENAME = 'testing.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

# just display a temporary homepage for now
def index(request):
    return render_to_response("map/index.html",
                              {},
                              context_instance=RequestContext(request))

def map(request):
    # just load the map
    logging.debug("Entered the \'map\' view...")
    return render_to_response("map/map.html",
                              {},
                              context_instance=RequestContext(request))

# View that saves a stop
def savestop(request):
    logging.debug("logging is working...")
    success = False
    error_msg = ""
    json_return_data = {}
    
    # If not a post, ignore
    if request.method != 'POST':
        logging.debug("Not a POST request, exiting...")
        error_msg = "You have reached this page in error...or need to send your data via POST"
        success = False
        json_return_data = {'success':success, 'error_msg':error_msg}
        return render_to_response("base.html",{'w_msg':error_msg})
        #HttpResponse(simplejson.dumps(json_return_data),mimetype='application/json')        

    logging.debug("about to get stuff from the POST request...")
#    logging.debug("GET items = " + str(request.GET.items()))

    # Make sure you have the required data
    stopLat = request.POST.__getitem__('lat')         #[0]['lat']
    logging.debug("lat = " + str(stopLat))    

    stopPicUrls = request.POST.getlist('urls[]')
    logging.debug("urls = " + str(stopPicUrls))

    stopLon = request.POST.__getitem__('lon')
    logging.debug("lon = " + str(stopLon))    
    stopTitle = request.POST.__getitem__('name')
    logging.debug("name = " + str(stopTitle))    

    # For now use the temp user: unknown
    unknown_user = User.objects.get(username='unknown')
    logging.debug("user = " + str(unknown_user.username))

    # Check for optional data
    stopDesc = ""
    if request.POST.__contains__('desc'):
        stopDesc = request.POST.__getitem__('desc')

    # Create the stop (the name is the title)
    stop = Stop(title=stopTitle,description=stopDesc,lat=stopLat,lon=stopLon,creator=unknown_user)
    stop.save()

    logging.debug("stop saved successfully...")

    # Create photos using the urls if they don't already exist
    for u in stopPicUrls:
        # if the photo exists, use that photo instead of saving a new one
        try:
            photo = Photo.objects.get(url=u)
            logging.debug("photo already exists...")
        except:
            # if photo doesn't exist, save the new Photo to the db
            # TODO: remove lat and lon fields from photos, or actually use them
            logging.debug("photo does not exist, adding to db")
            photo = Photo(url=u,lat=0.0,lon=0.0,uploaded_by=unknown_user)
            photo.save()
            
        # Once you have a photo, add it to the PhotosPerStop page
        try:
            pps = PhotosPerStop.objects.get(stop=stop,photo=photo)
            logging.debug("already exists in PPS table")
        except:
            logging.debug("new to PPS table")
            pps = PhotosPerStop(stop=stop,photo=photo)
            pps.save()
            logging.debug("saved photo into PPS")

    success = True
    error_msg = ""
    json_return_data['success'] = stop.id
    json_return_data['error_msg'] = ""   
    logging.debug("made it to the end of the view function....wooot???")
    response = HttpResponse(json.dumps(json_return_data),mimetype='application/json')
    logging.debug("response created successfully")
    return response
    

#def foo(request):
#    if request.method == 'POST':
#        form = Form1(request.POST)
#        if form.is_valid():
#            form.save()
#            if request.POST.get('type', '') == 'json':
#                data = {} # define your own data structure
#                return HttpResponse(simplejson.dumps(data),
#                                    mimetype='application/json')
#            else:
#                return HttpResponseRedirect('/foo/success/')
#    else:
#        form = Form1()
#    return render_to_response('app1/template1.html', {'form': form})
            
            
                
def saveroute(request):
    logging.debug("logging is working...")
    success = False
    error_msg = ""
    json_return_data = {}
    
    # If not a post, ignore
    if request.method != 'POST':
        logging.debug("Not a POST request, exiting...")
        error_msg = "You have reached this page in error...or need to send your data via POST"
        success = False
        json_return_data = {'success':success, 'error_msg':error_msg}
        return render_to_response("base.html",{'w_msg':error_msg})
        #HttpResponse(simplejson.dumps(json_return_data),mimetype='application/json')        

    logging.debug("about to get stuff from the POST request...")

    stopIds = request.POST.getlist('ids[]')
    logging.debug("stops = " + str(stopIds))

    # For now use the temp user: unknown
    unknown_user = User.objects.get(username='unknown')
    logging.debug("user = " + str(unknown_user.username))

    # Create the stop (the name is the title)
    route = Route(creator=unknown_user)
    route.save()

    logging.debug("routes saved successfully...")
    counter = 1
    # Create photos using the urls if they don't already exist
    for i in stopIds:
        try:
            stop = Stop.objects.get(id=i)
            logging.debug("stop already exists...")            
            # Once you have a route, add it to the StopPerRoute page
            spr = StopsPerRoute(route=route, stop=stop, routePosition=counter)
            counter += 1
        except:
            logging.debug("no such stop...")            
    success = True
    error_msg = ""
    json_return_data['success'] = "True"
    json_return_data['error_msg'] = ""   
    logging.debug("made it to the end of the view function....wooot???")
    response = HttpResponse(json.dumps(json_return_data),mimetype='application/json')
    logging.debug("response created successfully")
    return response
