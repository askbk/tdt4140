import { Filter } from "./filter.js";

/*
*   Filtrerer alle elementer med klasse "advert-item" basert på om de har tags
*   eller fritekst som matcher filteret.
*
*   Se filter.js for virkemåten til filterklassen.
*/

const advertFilter = new Filter(
    true,
    "advert-item",
    [
        "filter-checkbox-city",
        "filter-checkbox-tags"
    ],
    "search-input"
);
