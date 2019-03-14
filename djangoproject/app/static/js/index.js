import { Filter } from "./filter.js";

/*
*   Filtrerer alle elementer med klasse "content-item" basert på om de har tags
*   eller fritekst som matcher filteret.
*
*   Se filter.js for virkemåten til filterklassen.
*/

const startupFilter = new Filter(
    true,
    "content-item",
    [
        "filter-checkbox-type"
    ],
    "search-input"
);
