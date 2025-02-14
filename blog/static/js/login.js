document.addEventListener('DOMContentLoaded', function () {
    console.log("🛠️ login.js загружен!");

    const loginModal = document.getElementById('loginModal');
    const closeModal = loginModal ? loginModal.querySelector('.close') : null;
    const isAuthenticatedElement = document.getElementById('isAuthenticated');
    const contactForm = document.getElementById('contactForm');

    let modalTimeout; // Таймер для повторного появления окна

    // Функция центрирования окна
    function centerModal() {
        if (loginModal) {
            loginModal.style.display = 'flex';
            loginModal.style.alignItems = 'center';
            loginModal.style.justifyContent = 'center';
        }
    }

    // Проверка статуса авторизации
    const isAuthenticated = isAuthenticatedElement?.value === 'true';
    console.log("🔹 Статус авторизации (из Django):", isAuthenticated);

    // Блокируем отправку формы, если не авторизован
    if (contactForm && !isAuthenticated) {
        console.warn("⛔ Форма заблокирована, так как пользователь не авторизован.");
        contactForm.addEventListener('submit', function (event) {
            event.preventDefault();
            console.log("🔒 Открываем модальное окно входа...");
            loginModal.style.display = 'flex';
            centerModal();
        });

        // Отключаем кнопку отправки
        const submitButton = contactForm.querySelector('[type="submit"]');
        if (submitButton) {
            submitButton.disabled = true;
        }
    }

    // Закрытие окна и повторное появление через 2 секунды
    if (closeModal) {
        closeModal.addEventListener('click', () => {
            console.warn("⚠️ Окно закрыто! Появится снова через 2 секунды...");
            loginModal.style.display = 'none';

            // Через 2 сек появляется снова, если пользователь не авторизован
            clearTimeout(modalTimeout);
            modalTimeout = setTimeout(() => {
                if (!isAuthenticated) {
                    console.log("⏳ Показываем окно снова...");
                    loginModal.style.display = 'flex';
                    centerModal();
                }
            }, 2000);
        });
    }

    // Центрируем окно при загрузке
    if (loginModal) {
        centerModal();
    }
});
