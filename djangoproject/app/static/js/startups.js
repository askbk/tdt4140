import { Filter } from "./filter.js";

const startupFilter = new Filter(
    true,
    "startup-item",
    [
        "filter-checkbox-phase",
        "filter-checkbox-tags"
    ],
    "search-input"
);
