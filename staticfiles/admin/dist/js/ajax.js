document.body.addEventListener("click", function (event) {
    const link = event.target.closest("a");
    if (link && link.getAttribute("href") && link.getAttribute("href") !== "#") {
        let url = link.getAttribute("href");

        // Если клик по профилю, выполняем обычный переход (без AJAX)
        if (link.classList.contains("user-profile-link")) {
            return; // Позволяем стандартный переход
        }

        event.preventDefault();
        loadPage(url); // Остальные ссылки загружаем через AJAX
    }
});

// Функция для загрузки контента через AJAX
function loadPage(url) {
    fetch(url, { headers: { "X-Requested-With": "XMLHttpRequest" } })
        .then(response => response.text())
        .then(html => {
            let parser = new DOMParser();
            let doc = parser.parseFromString(html, "text/html");
            let newContent = doc.querySelector(".content-wrapper").innerHTML;

            document.querySelector(".content-wrapper").innerHTML = newContent;
            history.pushState({ path: url }, "", url);

            // 🔹 Вызов обновления меню
            updateActiveMenu();
            bindAjaxForms();
            bindDeleteButtons();
            bindUpdateButtons();

            // 🔥 Добавляем событие AJAX-завершения
            document.dispatchEvent(new Event("ajaxComplete"));
        })
        .catch(error => console.error("Ошибка при загрузке страницы:", error));
}


// Обработчик кнопок "назад/вперёд" в браузере
window.addEventListener("popstate", function () {
    loadPage(location.href);
});

// Обновление активного меню
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
            if (parentTree) parentTree.style.display = "block";
        }
    });
}

// Функция для привязки AJAX-форм
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
                updateActiveMenu();
                bindAjaxForms();
                bindDeleteButtons();
                bindUpdateButtons();

                let redirectUrl = form.getAttribute("data-redirect");
                if (redirectUrl) {
                    history.pushState({ path: redirectUrl }, "", redirectUrl);
                }
            })
            .catch(error => console.error("Ошибка при отправке формы:", error));
        });
    });
}

// Привязываем обработчики удаления
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
                    if (deletedRow) deletedRow.remove();
                    updateActiveMenu();
                } else {
                    alert("Ошибка при удалении!");
                }
            })
            .catch(error => console.error("Ошибка при удалении:", error));
        });
    });
}

// Привязываем обработчики обновления
function bindUpdateButtons() {
    document.querySelectorAll(".update-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();
            let updateUrl = this.getAttribute("href");
            loadPage(updateUrl);
        });
    });
}

// Инициализация
updateActiveMenu();
bindAjaxForms();
bindDeleteButtons();
bindUpdateButtons();
