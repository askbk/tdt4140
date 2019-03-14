import { Filter } from "./filter.js";

/*
*   Filtrerer alle elementer med klasse "investor-item" basert på om de har tags
*   eller fritekst som matcher filteret.
*
*   Se filter.js for virkemåten til filterklassen.
*/

const investorFilter = new Filter(
    true,
    "investor-item",
    [
        "filter-checkbox-tags"
    ],
    "search-input"
);
