document.addEventListener("DOMContentLoaded", function () {
    console.log("Admin profile script initialized!");

    function enableEditing() {
        document.querySelectorAll(".editable").forEach(el => el.classList.remove("d-none"));
        document.querySelector("#avatar-field")?.classList.remove("d-none");
        document.querySelector("#edit-btn")?.classList.add("d-none");
        document.querySelector("#save-btn")?.classList.remove("d-none");
        document.querySelector("#cancel-btn")?.classList.remove("d-none");
    }

    function cancelEditing() {
        document.querySelectorAll(".editable").forEach(el => el.classList.add("d-none"));
        document.querySelector("#avatar-field")?.classList.add("d-none");
        document.querySelector("#edit-btn")?.classList.remove("d-none");
        document.querySelector("#save-btn")?.classList.add("d-none");
        document.querySelector("#cancel-btn")?.classList.add("d-none");
    }

    function loadFullPage(url) {
        // Полностью загружаем страницу
        window.location.href = url;
    }

    document.querySelectorAll(".ajax-link").forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            let url = this.getAttribute("href");
            loadFullPage(url); // Переход на страницу с полной загрузкой
        });
    });

    window.enableEditing = enableEditing;
    window.cancelEditing = cancelEditing;
});
