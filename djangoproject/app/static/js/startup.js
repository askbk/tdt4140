/*
*   Viser kart med posisjonen til startupen
*/
window.onload = () => {
    const createMap = (error, response) => {
        //  Henter koordinater basert på addressen til startupen
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

        //  Legger til markør på posisjonen
        L.marker(latLng, {
            icon: L.mapquest.icons.marker(),
            draggable: false,
        }).bindPopup(popupText).addTo(map);

        //  Legger til kartkontroll
        map.addControl(L.mapquest.control());
    }

    //  API-key
    L.mapquest.key = '3Ahbrjn0yAjeG9gQgTTSRu4ubu2LXDB4';

    L.mapquest.geocoding().geocode(address, createMap);
}
