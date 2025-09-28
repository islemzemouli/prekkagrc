function initialize() {
  var myOptions = {
    zoom: 15,
    center: new google.maps.LatLng(35.555, 6.1741), // Batna coordinates
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    scrollwheel: false,
    mapTypeControl: false,
    zoomControl: false,
    streetViewControl: false,
  };
  var map = new google.maps.Map(
    document.getElementById("map-canvas"),
    myOptions
  );
  var marker = new google.maps.Marker({
    map: map,
    position: new google.maps.LatLng(35.555, 6.1741), // Batna marker
  });
}
google.maps.event.addDomListener(window, "load", initialize);
