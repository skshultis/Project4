$(document).ready(function()  {

// L.mapbox.accessToken = 'pk.eyJ1Ijoic2tzaHVsdGlzIiwiYSI6ImNpdDJ3a2JtYTB0cHEycHFwOW5uMGV5cHkifQ.sUGo-LKDrCEO_LEhsCmqXQ';
// var map = L.mapbox.map('skshultis.7jru2v1l', {
//     center: [38.892523, -76.995845],
//     zoom: 11
// });
mapboxgl.accessToken = 'pk.eyJ1Ijoic2tzaHVsdGlzIiwiYSI6ImNpdDJ3a2JtYTB0cHEycHFwOW5uMGV5cHkifQ.sUGo-LKDrCEO_LEhsCmqXQ';
// This shows the map
var map = new mapboxgl.Map({
  // container id specified in the HTML
  container: 'map',
  style: 'mapbox://styles/skshultis/cit4ctt95000d2xo1mcmu1pes',
  // initial position and zoom
  center: [-76.995845, 38.892523],
  zoom: 11.3
});

// map.on('load', function (e) {
//   // Add the stores data as a source
//   map.addSource("places", {
//     "type": "geojson",
//     "data": incidents
//   });
//
// 	// Add a layer to the map with styling rules to render the source
// 	map.addLayer({
//     "id": "locations",
//     "type": "circle",
//     "source": "places",
//     "layout": {
//       "icon-image": "restaurant-15",
//       "icon-allow-overlap": true,
//     }
//   });
// });
//

});
