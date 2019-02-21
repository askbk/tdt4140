window.onload = () => {
    const createMap = (error, response) => {
        const location = response.results[0].locations[0];
        const latLng = location.displayLatLng;
        const map = L.mapquest.map(
            'map',
            {
                center: latLng,
                layers: L.mapquest.tileLayer('map'),
                zoom: 14
            }
        );

        L.marker(latLng, {
            icon: L.mapquest.icons.marker(),
            draggable: false,
        }).bindPopup(popupText).addTo(map);

        map.addControl(L.mapquest.control());
    }

    L.mapquest.key = '3Ahbrjn0yAjeG9gQgTTSRu4ubu2LXDB4';

    L.mapquest.geocoding().geocode(address, createMap);


    /*{street: "{{profile.address.street_address|a_to_a}}",
    city: "{{profile.address.city|a_to_a}}",
    postalCode: {{profile.address.postal_code}},
    adminArea1Type: "{{profile.address.country|a_to_a}}",
    }, createMap);*/
}
