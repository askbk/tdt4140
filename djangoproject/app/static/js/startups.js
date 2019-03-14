import { Filter } from "./filter.js";

/*
*   Filtrerer alle elementer med klasse "startup-item" basert på om de har tags
*   eller fritekst som matcher filteret.
*
*   Se filter.js for virkemåten til filterklassen.
*/

const startupFilter = new Filter(
    true,
    "startup-item",
    [
        "filter-checkbox-phase",
        "filter-checkbox-tags"
    ],
    "search-input"
);
