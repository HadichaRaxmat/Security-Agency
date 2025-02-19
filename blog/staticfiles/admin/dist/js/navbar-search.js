document.addEventListener("DOMContentLoaded", function () {
    const toggleSearch = document.getElementById("toggle-search");
    const searchBlock = document.querySelector(".navbar-search-block");
    const searchInput = document.getElementById("search-input");
    const closeSearch = document.getElementById("close-search");
    const searchResults = document.getElementById("search-results");

    // Открытие/закрытие поиска
    toggleSearch.addEventListener("click", function (e) {
        e.preventDefault();
        searchBlock.style.display = searchBlock.style.display === "none" ? "block" : "none";
        searchInput.focus();
    });

    // Закрытие поиска
    closeSearch.addEventListener("click", function () {
        searchBlock.style.display = "none";
        searchResults.style.display = "none";
        searchInput.value = "";
        clearHighlights();
    });

    // Очистка предыдущих подсветок
    function clearHighlights() {
        document.querySelectorAll(".highlight").forEach(el => {
            el.outerHTML = el.innerText;
        });
    }

    // Поиск и подсветка слов
    searchInput.addEventListener("input", function () {
        let query = this.value.toLowerCase();
        searchResults.innerHTML = "";
        searchResults.style.display = "none";
        clearHighlights();

        if (query.trim() === "") return;

        let foundElements = [];
        let elements = document.body.querySelectorAll("*:not(script):not(style)");

        elements.forEach(el => {
            if (el.childNodes.length === 1 && el.childNodes[0].nodeType === 3) {
                let text = el.textContent;
                if (text.toLowerCase().includes(query)) {
                    let regex = new RegExp(query, "gi");
                    el.innerHTML = text.replace(regex, match => `<span class="highlight">${match}</span>`);
                    foundElements.push(el);
                }
            }
        });

        // Прокрутка к первому найденному элементу
        if (foundElements.length > 0) {
            foundElements[0].scrollIntoView({ behavior: "smooth", block: "center" });

            // Заполнение выпадающего списка
            foundElements.forEach((el, index) => {
                let listItem = document.createElement("li");
                listItem.classList.add("dropdown-item");
                listItem.innerHTML = el.textContent;
                listItem.addEventListener("click", function () {
                    el.scrollIntoView({ behavior: "smooth", block: "center" });
                });
                searchResults.appendChild(listItem);
            });

            searchResults.style.display = "block";
        }
    });
});
