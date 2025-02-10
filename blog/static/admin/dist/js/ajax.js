document.addEventListener("DOMContentLoaded", function () {
    function updateActiveMenu() {
        let currentUrl = window.location.pathname;
        document.querySelectorAll(".nav-link").forEach(link => {
            let linkUrl = new URL(link.href, window.location.origin).pathname;
            link.classList.remove("active");
            if (currentUrl.startsWith(linkUrl)) {
                link.classList.add("active");
                let parentItem = link.closest(".nav-item");
                if (parentItem) parentItem.classList.add("menu-open");
                let parentTree = link.closest(".nav-treeview");
                if (parentTree) parentTree.style.display = "block"; // открываем подменю
            }
        });
    }

    // Загрузка новой страницы через AJAX
    function loadPage(url) {
        fetch(url, { headers: { "X-Requested-With": "XMLHttpRequest" } })
            .then(response => response.text())
            .then(html => {
                let parser = new DOMParser();
                let doc = parser.parseFromString(html, "text/html");
                let newContent = doc.querySelector(".content-wrapper").innerHTML;
                document.querySelector(".content-wrapper").innerHTML = newContent;
                history.pushState(null, "", url); // Изменение истории

                updateActiveMenu();  // Обновляем активное меню
                bindAjaxForms();  // Обновляем обработчики форм
                bindDeleteButtons(); // Обновляем обработчики удаления
                bindUpdateButtons(); // Обновляем обработчики кнопок обновления
            })
            .catch(error => console.error("Ошибка загрузки страницы:", error));
    }

    // Обработчик переходов по ссылкам с использованием AJAX
    document.body.addEventListener("click", function (event) {
        const link = event.target.closest("a");
        if (link && link.getAttribute("href") && link.getAttribute("href") !== "#") {
            event.preventDefault();
            loadPage(link.href); // Загружаем страницу через AJAX
        }
    });

    window.addEventListener("popstate", function () {
        loadPage(location.href); // Обработчик кнопок назад/вперед
    });

    // Обработчики для динамических форм
    function bindAjaxForms() {
        document.querySelectorAll("form.ajax-form").forEach(form => {
            form.addEventListener("submit", function (event) {
                event.preventDefault();
                let formData = new FormData(form);
                let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
                let postUrl = form.getAttribute("action");

                fetch(postUrl, {
                    method: "POST",
                    body: formData,
                    headers: { "X-CSRFToken": csrfToken }
                })
                .then(response => response.text())
                .then(html => {
                    let parser = new DOMParser();
                    let doc = parser.parseFromString(html, "text/html");
                    let newContent = doc.querySelector(".content-wrapper").innerHTML;
                    document.querySelector(".content-wrapper").innerHTML = newContent;
                    updateActiveMenu();  // Обновление меню после отправки формы
                    bindAjaxForms();  // Повторное привязывание обработчиков форм
                    bindDeleteButtons(); // Обновление кнопок удаления
                    bindUpdateButtons(); // Обновление кнопок обновления
                })
                .catch(error => console.error("Ошибка при отправке формы:", error));
            });
        });
    }

    // Обработчики для кнопок удаления
    function bindDeleteButtons() {
        document.querySelectorAll(".delete-btn").forEach(button => {
            button.addEventListener("click", function (event) {
                event.preventDefault();
                if (!confirm("Вы уверены, что хотите удалить?")) return;

                let deleteUrl = this.getAttribute("href");
                let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

                fetch(deleteUrl, {
                    method: "POST",
                    headers: { "X-CSRFToken": csrfToken, "X-Requested-With": "XMLHttpRequest" }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        let deletedRow = document.querySelector(`[data-id="${data.deleted_id}"]`);
                        if (deletedRow) deletedRow.remove(); // Удаляем из списка
                        updateActiveMenu(); // Обновляем меню после удаления
                    } else {
                        alert("Ошибка при удалении!");
                    }
                })
                .catch(error => console.error("Ошибка при удалении:", error));
            });
        });
    }

    // Обработчики для кнопок обновления
    function bindUpdateButtons() {
        document.querySelectorAll(".update-btn").forEach(button => {
            button.addEventListener("click", function (event) {
                event.preventDefault();
                let updateUrl = this.getAttribute("href");
                loadPage(updateUrl); // Загружаем страницу для обновления
            });
        });
    }

    // Инициализация при загрузке страницы
    updateActiveMenu(); // Обновляем активное меню
    bindAjaxForms(); // Привязываем обработчики форм
    bindDeleteButtons(); // Привязываем обработчики удаления
    bindUpdateButtons(); // Привязываем обработчики обновления
});