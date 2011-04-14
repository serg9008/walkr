 var map;
  var geocoder;
  var f_url = "http://api.flickr.com/services/rest/?method=";
  var api_key = "&api_key=4bf1b9bd80cd8fe69d1800dcad2355ac"
  var format_json = "&format=json&jsoncallback=?";
  var stopList = new Array();
  var currPhoto = new Array();
  var flowInstance = new ImageFlow();

  function Photo(name, lat, lng) {
	  this.name= name;
	  this.lat = lat;
	  this.lng = lng;
  }
  
  function getFickrPhotos(url, show_marker, lat, lng, repeat) {
      $("#imageSlider").empty();
	  $("#imageSlider").show();
	  currPhoto = new Array();
	  flowInstance = new ImageFlow();	
	  $.getJSON(url, function(data) {
		  var num = data.photos.photo.length;
		  $.each(data.photos.photo, function(index, photo) {
			$.getJSON(f_url + "flickr.photos.geo.getLocation" + api_key + "&photo_id=" + photo.id + format_json,
				function(loc_data) {
					var pLat = loc_data.photo.location.latitude;
					var pLng = loc_data.photo.location.longitude;
					$.getJSON(f_url + "flickr.photos.getSizes" + api_key + "&photo_id=" + photo.id + format_json,
						function(p_data) {
							$("#imageSlider").append("<img id='img" + photo.id + "' class='image-drag' src='" + p_data.sizes.size[2].source + "'</img>");					
							currPhoto['img' + photo.id]=(new Photo('img' + photo.id, pLat, pLng));
							
							 //$( "#img" + photo.id ).bind("mousedown", function(evt) {
							 //if(evt.preventDefault)
							//	evt.preventDefault();});
							if(num-1 == index) 
							{
								var circ = false;
								if(num > 4)
									circ = true;												
								flowInstance.init({ ImageFlowID:'imageSlider', circular:circ, reflections:false, slider:false, aspectRatio: 6, xStep: 100, opacity: true, 
									opacityArray: [10, 10, 9, 8, 7], 
									onClick: function(){}});	
								$("#imageSlider img").each(function() {
									$(this).draggable({
										appendTo: 'body',
										activeClass: "image-drag-active",
										revert: "invalid", // when not dropped, the item will revert back to its initial position
										helper: "clone",
										cursor: "move"
									});
									var marker = new google.maps.Marker({
										position: new google.maps.LatLng(currPhoto[$(this).attr('id')].lat,currPhoto[$(this).attr('id')].lng),
										icon: 'images/camera_icon.png'
									});
									$(this).hover(function() {marker.setMap(map);}, function() {marker.setMap(null);})}
								);
								if(num == 1)
									$("#imageSlider_images img").css("z-index", "1 !important");
							}
							/*$("#img" + photo.id).click(function() {info.open(map, marker)});
							marker.setMap(map); 
							google.maps.event.addListener(marker, 'click', function() {
								info.open(map, marker);
						
												});*/
									  });
							 });
			 });                                         
			  if (show_marker && num > 0 && !repeat) {
					$("#buttons").hide();
					var button = $("<button>Delete Point</button>");
					$("#deletePointButton").empty();
					$("#deletePointButton").append(button);
					button.button();
					var removeMarker = function() {
						marker.setMap(null);
						button.remove();
						clearPhotoContainer();
						$("#buttons").hide();
						$("#imageSlider").hide();
					};
					button.click(removeMarker);
					
					clearPhotoContainer(); 
					var marker = new google.maps.Marker({
						position: new google.maps.LatLng(lat,lng)
					});
					var info = new google.maps.InfoWindow({
								content: ""
							});
					marker.setMap(map); 
					google.maps.event.addListener(marker, 'click', function() {
							getPhotosForPoint(lat, lng, 0.08, true);
							$("#deletePointButton").empty();
							button.button();
							button.click(removeMarker);
							$("#deletePointButton").append(button);
							//info.open(map, marker);
							});
			}
		 });
  }
  function getPhotosForPoint(lat, lng, radius, repeat) {
	url = f_url + "flickr.photos.search" + api_key;
	url += "&lat=" +lat;
	url += "&lon=" +lng;
	url += "&min_upload_date=01-1-1";
	url += "&per_page=20";
	url += "&radius=" +radius;
	url += "&has_geo=true";
	url += format_json;
	getFickrPhotos(url, true, lat, lng, repeat);
  }
  
  function flickrCall() {
	var bounds = map.getBounds();
	url = f_url + "flickr.photos.search" + api_key;
	url += "&tags=iu";
	url += "&per_page=10";
	url += "&has_geo=true";
	url += "&bbox=" + bounds.getSouthWest().lng() + "," + bounds.getSouthWest().lat() + "," +  
			  bounds.getNorthEast().lng() + "," + bounds.getNorthEast().lat(); 
	url += format_json;
	getFickrPhotos(url, false);
	
 }

   function addImage(item, container) {
	var el = $("#photoContainer #" + $(item).attr('id'));
	var el2 = $("#" + $(container).attr('id') + " img");
	if(el.length || el2.length)
		return;
    var nimgHeight = 75;
	var h = parseInt($(item).css('height'));
	var diff = (nimgHeight)/h;
	var imgWidth = parseInt($(item).css('width'));
	var imgDivBg = $('<div></div>');
	$(imgDivBg).css('height', (nimgHeight)+"px");
	$(imgDivBg).css('width', (imgWidth*diff)+"px" );
	$(item).css('z-index', "10 !important");
	$(item).addClass('image-not-over');
	$(container).removeClass('drag-bg');
	item.appendTo(imgDivBg);
	$("#buttons").show();
	imgDivBg.appendTo(container).fadeIn(function() {
					item.animate({ height: (nimgHeight)+"px", width: (imgWidth*diff)+"px"},
									function() {
										$(item).mouseover(function() {
											$(item).addClass('image-over');
											$(item).removeClass('image-not-over');
											$(container).addClass('image-delete');
											});
										$(item).mouseout(function() {
											$(item).removeClass('image-over');
											$(item).addClass('image-not-over');
											$(container).removeClass('image-delete');
										});
										$(item).click(function() {
											$(imgDivBg).remove();
											var el = $("#photoContainer img");
											$(container).addClass('drag-bg');
											if(!el.length)
											{
												$("#buttons").hide();
											}	
										});
									});
	});
 }
 
 function clearPhotoContainer() {
	$("#photoContainer td").each(function() {
			$(this).empty();
			$(this).addClass('drag-bg');
		});
 }

  function initialize() {
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(39.171235,-86.514959);
    var myOptions = {
      zoom: 16,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map_canvas"),
        myOptions);
	google.maps.event.addListener
        (map, 'click', function(location) {
			getPhotosForPoint(location.latLng.lat(), location.latLng.lng(), 0.08, false);
		});
	map.setOptions({ draggableCursor: 'crosshair' });
	
    $( "#tabs" ).tabs();
	$("#saveButton").button();
        $("#saveButton").click(function() {
             var urlsArray = new Array();
             var photo;
             $("#photoContainer img").each(function() {
            	 urlsArray.push($(this).attr('src')); 
            	 photo = currPhoto[$(this).attr('id')];
              });
             $.getJSON('http://127.0.0.1:8000/walkr/savestop', 
                    { urls: urlsArray, lat: photo.lat, lon: photo.lng, name: photo.name}, function(data) {
                      alert(data);
                    });
           });
	$("#cancelButton").button();
	$("#cancelButton").click(function() { 
		clearPhotoContainer();
		$("#buttons").hide();
	});
	$("#loginButton").button();
	$("#registerButton").button();
	$("#searchButton").button();
	$('#search-form').submit(function() {
  		var searchForm = $("#search-form").serializeArray();
		if(searchForm[1].value == "Map" && searchForm[0].value != "")
		{
			geocoder.geocode( { 'address': searchForm[0].value}, function(results, status) {
		        if (status == google.maps.GeocoderStatus.OK) {
				map.setCenter(results[0].geometry.location);
		      } else {
				alert("Geocode was not successful for the following reason: " + status);
		      }
		    });
		}
		return false;
	});
	$("#searchButton").click(function() {
		$('#search-form').submit();
	});
	$("#buttons").hide();
	
	$("#photoContainer td").each(function() {
		var container = $(this);
		container.droppable({
			accept: ".image-drag",
			tolerance: 'pointer',
			drop: function( event, ui ) {
				addImage( $(ui.draggable).clone(), container );
			}
		});
	});
  }
