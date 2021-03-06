/*
*   Klasse for å filtrere elementer.
*
*   Fritekst-søket baserer seg på innholdet i "data-text"-attributtet til
*   elementene, sjekkboks-tags baserer seg på innholdet i
*   "data-tags"-attributtet til elementene.
*
*   Filteret baserer seg på følgende logikk:
*       - Filtreringskriterier er delt opp i "grupper":
*           - Kan f.eks. være sjekkbokser som alle handler om by
*       - Dersom en gruppe ikke er aktiv, blir den ikke tatt hensyn til i filtreringen
*           - F.eks. er en gruppe sjekkbokser inaktive dersom ingen av dem er huket av
*       - Et element vises dersom følgende er sant:
*           - "data-text" inneholder alle ord som er skrevet i søkeføltet
*           - "data-tags" inneholder minst én av tagsene som er huket av per gruppe
*/

export class Filter {
    constructor(DEBUG_MODE, itemSelector, filterCheckboxSelectors, searchBoxSelector) {
        this.DEBUG_MODE = DEBUG_MODE;

        //  Elementer som skal filtreres blant
        this.items = document.getElementsByClassName(itemSelector);

        //  Array med klassenavn for hver sjekkboks-gruppe
        this.filterCheckboxSelectors = filterCheckboxSelectors;

        //  Søkefeltet
        this.searchBox = document.getElementById(searchBoxSelector);

        //  Array som inneholder array av sjekkboksgrupper
        this.filterCheckboxGroups = [];
        for (let selector of filterCheckboxSelectors) {
            this.filterCheckboxGroups.push(
                document.getElementsByClassName(selector)
            );
        }

        //  Opprett nytt sett for hver filtreringsgruppe og legg til
        //  eventlistener på alle checkboxes.
        this.filters = [];
        for (let checkboxGroup of this.filterCheckboxGroups) {
            this.filters.push(new Set());

            for (let checkbox of checkboxGroup) {
                checkbox.addEventListener(
                    "change",
                    this.checkHandler.bind(this, checkbox)
                );
            }
        }

        //  Dersom man skal bruke en søkeboks
        if (this.searchBox) {
            this.freetext = new Set();
            this.searchBox.addEventListener(
                "keyup",
                this.searchHandler.bind(this)
            );
        }
    }

    //  Går gjennom hver filtercheckboxgroup og sjekker at minst én tag fra
    //  hver filtreringsgruppe er tilstede.
    //  Sjekker så at alt fra freetext er tilstede i tittelen.
    handleItem(item) {
        const tags = new Set(item.dataset.tags.split("+"));

        if (this.DEBUG_MODE) {
            console.log("---\n item is tagged with");
            console.log(tags);
        }

        for (let filter of this.filters) {
            if (this.zeroIntersection(filter, tags)) {
                item.style.display = "none";
                return;
            }
        }

        if (this.searchBox) {
            const text = item.dataset.text.toLowerCase();

            if (this.DEBUG_MODE) {
                console.log("---\n item has text:");
                console.log(text);
                console.log("matching agains set:");
                console.log(this.freetext);
            }

            if (!this.isContained(text, this.freetext)) {
                item.style.display = "none";
                return;
            }
        }

        item.style.display = "block";
    }

    //  Event handler for endring av checkboxes
    checkHandler(el, e) {
        const filterGroup = el.classList[0];

        for (let i = 0, len = this.filterCheckboxSelectors.length; i < len; i++) {
            if (filterGroup === this.filterCheckboxSelectors[i]) {
                if (el.checked) {
                    this.filters[i].add(el.name);
                } else {
                    this.filters[i].delete(el.name);
                }
            }
        }

        if (this.DEBUG_MODE) {
            console.log("using filter:");
            console.log(this.filters);
        }

        for (let i = 0, len = this.items.length; i < len; i++) {
            this.handleItem(this.items[i]);
        }
    }

    //  Event handler for søkefelt
    searchHandler() {
        this.freetext = new Set(this.searchBox.value.toLowerCase().split(" "));

        for (let i = 0, len = this.items.length; i < len; i++) {
            this.handleItem(this.items[i]);
        }
    }

    //  Sjekker om filtertags er tilstede for et item.
    zeroIntersection(setA, setB) {
        if (setA.size === 0) {
            //  Returnerer false for at filteret ikke skal ha noen virkning
            //  dersom det er tomt.
            return false;
        }

        for (const el of setB) {
            if (setA.has(el)) {
                return false;
            }
        }
        return true;
    }

    //  Sjekker om elementer fra set er inneholdt i strengen
    isContained(text, set) {
        for (let el of set) {
            if (text.indexOf(el) === -1) {
                return false;
            }
        }

        return true;
    }

}
