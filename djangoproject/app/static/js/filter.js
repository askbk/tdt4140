export class Filter {
    constructor(itemSelector, mode = "or") {
        this.filterCheckboxes = document.getElementsByClassName("filter-checkbox");
        this.items = document.getElementsByClassName(itemSelector);
        this.mode = mode;
        this.filters = new Set();

        for (let i = 0, len = this.filterCheckboxes.length; i < len; i++) {
            let el = this.filterCheckboxes[i];
            el.addEventListener("change", this.changeHandler.bind(this, el));
        }
    }

    handleItem(item) {
        const tags = new Set(item.dataset.tags.split());
        for (let filterTag of this.filters) {
            if (!tags.has(filterTag)) {
                item.style.display = "none";
                return;
            }
        }

        item.style.display = "block";
    }

    resetFilter() {
        for (let i = 0, len = this.items.length; i < len; i++) {
            this.items[i].style.display = "block";
        }
    }

    changeHandler(el, e) {
        if (el.checked) {
            this.filters.add(el.name);
        } else {
            this.filters.delete(el.name);
        }

        if (this.filters.size > 0) {
            for (let i = 0, len = this.items.length; i < len; i++) {
                this.handleItem(this.items[i]);
            }
        } else {
            this.resetFilter();
        }
    }
}
