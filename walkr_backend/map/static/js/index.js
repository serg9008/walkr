$(document).ready(function() {

    $( "#tabs" ).tabs();
	$( "#main_tabs" ).tabs();
	$("#saveButton").button();
	$("#serachRoutesButton").button();
	$("#cancelButton").button();
	$("#cancelButton").click(function() { 
		clearPhotoContainer();
		$("#buttons").hide();
	});
	$("#loginButton").button();
	$("#registerButton").button();
	$("#searchButton").button();
	$("#buttons").hide();
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
	
});