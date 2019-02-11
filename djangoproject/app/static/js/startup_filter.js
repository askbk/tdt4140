const filterCheckboxes = document.getElementsByClassName("filter-checkbox"),    //  Henter alle filter-checkboxes
    startups = [];  //  Variabel for å holde startups som er hentet fra django
let filters = new Set();    //  Mengde av filter som er i bruk

//  Loop gjennom og legg til eventlistener som skal anvende eller fjerne filtre som er i bruk
for (let i = 0, len = filterCheckboxes.length; i < len; i++) {
    let el = filterCheckboxes[i];
    el.addEventListener("change", e => {
        if (el.checked) {
            filters.add(el.name);
        } else {
            filters.delete(el.name);
        }
        console.log(filters);
    });
}
