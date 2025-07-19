let map;
let resMarker, delMarker;

function initMap() {
    const center = { lat: 11.1271,lng:78.6569 }; // Bangalore

    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 12,
        center: center,
    });
    // map.js
document.addEventListener('DOMContentLoaded', function () {
    const tamilNaduCoords = [11.1271, 78.6569];
    const map = L.map('map').setView(tamilNaduCoords, 7);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
    }).addTo(map);

    L.marker(tamilNaduCoords).addTo(map)
        .bindPopup('Tamil Nadu')
        .openPopup();
});


    map.addListener("click", (e) => {
        if (!resMarker) {
            resMarker = new google.maps.Marker({
                position: e.latLng,
                map: map,
                label: "R",
                title: "Restaurant Location"
            });
            document.getElementById("restaurant_lat").value = e.latLng.lat();
            document.getElementById("restaurant_lon").value = e.latLng.lng();
        } else if (!delMarker) {
            delMarker = new google.maps.Marker({
                position: e.latLng,
                map: map,
                label: "D",
                title: "Delivery Location"
            });
            document.getElementById("delivery_lat").value = e.latLng.lat();
            document.getElementById("delivery_lon").value = e.latLng.lng();
        } else {
            alert("Both locations already selected. Refresh to reselect.");
        }
    });
}
