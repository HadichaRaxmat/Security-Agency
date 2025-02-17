document.addEventListener("DOMContentLoaded", function () {
    function updateActiveMenu() {
        let currentUrl = window.location.pathname;
        console.log("🔄 Обновление меню. Текущий URL:", currentUrl);

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

        // Проверяем родительские пункты
        document.querySelectorAll(".nav-item > .nav-link").forEach(parent => {
            let submenu = parent.nextElementSibling;
            if (submenu && submenu.classList.contains("nav-treeview")) {
                let hasActiveChild = submenu.querySelector(".nav-link.active");
                parent.classList.toggle("active", !!hasActiveChild);
                parent.classList.toggle("menu-open", !!hasActiveChild);
            }
        });
    }

    // Вызываем при загрузке страницы
    updateActiveMenu();

    // 🔹 Поддержка AJAX-загрузки
    document.addEventListener("ajaxComplete", function () {
        console.log("⚡ AJAX завершен. Обновляем меню.");
        setTimeout(updateActiveMenu, 100);
    });

    // 🔹 Обновление меню при нажатии на ссылки
    document.body.addEventListener("click", function (event) {
        let link = event.target.closest(".nav-link");
        if (link) {
            setTimeout(updateActiveMenu, 100);
        }
    });

    // 🔹 Поддержка кнопок "назад/вперед"
    window.addEventListener("popstate", updateActiveMenu);

    // 🔹 Следим за изменениями в DOM (если меню обновляется динамически)
    const observer = new MutationObserver(updateActiveMenu);
    observer.observe(document.querySelector(".sidebar"), { childList: true, subtree: true });
});
