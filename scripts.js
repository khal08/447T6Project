function getMapboxTiles(map_type)
{
	return L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{type}/tiles/{z}/{x}/{y}?access_token={token}",
		{
			attribution: "Map data &copy;<a href='https://openstreetmap.org/copyright'>OpenStreetMap</a> contributors, Imagery &copy;<a href='https://www.mapbox.com/'>Mapbox</a>",
			type: map_type,
			tileSize: 512,
			zoomOffset: -1,
			token: "pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",
		});
}