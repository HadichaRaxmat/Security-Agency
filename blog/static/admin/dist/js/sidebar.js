document.addEventListener("DOMContentLoaded", function () {
    function updateActiveMenu() {
        let currentUrl = window.location.pathname;
        console.log("Current URL:", currentUrl);

        document.querySelectorAll(".nav-link").forEach(link => {
            let linkUrl = new URL(link.href, window.location.origin).pathname;
            link.classList.remove("active");

            if (currentUrl === linkUrl) {
                link.classList.add("active");

                let parentItem = link.closest(".nav-item");
                if (parentItem) {
                    parentItem.classList.add("menu-open");
                }

                let parentTree = link.closest(".nav-treeview");
                if (parentTree) {
                    parentTree.style.display = "block";
                }
            }
        });

        // Проверяем родительские пункты (Dashboard и DataTables)
        document.querySelectorAll(".nav-item > .nav-link").forEach(parent => {
            let submenu = parent.nextElementSibling;
            if (submenu && submenu.classList.contains("nav-treeview")) {
                let hasActiveChild = submenu.querySelector(".nav-link.active");
                if (hasActiveChild) {
                    parent.classList.add("active", "menu-open");
                } else {
                    parent.classList.remove("active");
                }
            }
        });
    }

    updateActiveMenu();
});
