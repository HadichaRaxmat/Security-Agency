document.addEventListener("DOMContentLoaded", function () {
    console.log("🛠️ login.js загружен!");

    const loginModal = document.getElementById("loginModal");
    const registerModal = document.getElementById("registerModal");
    const closeButtons = document.querySelectorAll(".close");
    const showRegister = document.querySelector(".register-link");
    const showLogin = document.getElementById("showLogin");
    const isAuthenticatedElement = document.getElementById("isAuthenticated");
    const contactForm = document.getElementById("contactForm");

    let modalTimeout; // Таймер для повторного появления окна

    // Функция центрирования окна
    function showModal(modal) {
        if (modal) {
            modal.style.display = "flex";
            modal.style.alignItems = "center";
            modal.style.justifyContent = "center";
        }
    }

    function hideModal(modal) {
        if (modal) {
            modal.style.display = "none";
        }
    }

    // Проверка статуса авторизации
    const isAuthenticated = isAuthenticatedElement?.value === "true";
    console.log("🔹 Статус авторизации:", isAuthenticated);

    // Блокируем отправку формы, если не авторизован
    if (contactForm && !isAuthenticated) {
        console.warn("⛔ Форма заблокирована, так как пользователь не авторизован.");
        contactForm.addEventListener("submit", function (event) {
            event.preventDefault();
            console.log("🔒 Открываем модальное окно входа...");
            showModal(loginModal);
        });

        // Отключаем кнопку отправки
        const submitButton = contactForm.querySelector("[type='submit']");
        if (submitButton) {
            submitButton.disabled = true;
        }
    }

    // Закрытие окон и их повторное появление через 2 секунды
    closeButtons.forEach(button => {
        button.addEventListener("click", function () {
            console.warn("⚠️ Окно закрыто! Появится снова через 2 секунды...");
            hideModal(loginModal);
            hideModal(registerModal);

            // Через 2 сек появляется снова, если пользователь не авторизован
            clearTimeout(modalTimeout);
            modalTimeout = setTimeout(() => {
                if (!isAuthenticated) {
                    console.log("⏳ Показываем окно снова...");
                    showModal(loginModal);
                }
            }, 2000);
        });
    });

    // Переключение между формами входа и регистрации
    if (showRegister) {
        showRegister.addEventListener("click", function (e) {
            e.preventDefault();
            hideModal(loginModal);
            showModal(registerModal);
        });
    }

    if (showLogin) {
        showLogin.addEventListener("click", function (e) {
            e.preventDefault();
            hideModal(registerModal);
            showModal(loginModal);
        });
    }

    // Закрытие при клике вне модального окна
    window.addEventListener("click", function (event) {
        if (event.target.classList.contains("modal")) {
            hideModal(event.target);
        }
    });

    // Открываем модальное окно входа при загрузке, если пользователь не авторизован
    if (loginModal && !isAuthenticated) {
        showModal(loginModal);
    }
});
