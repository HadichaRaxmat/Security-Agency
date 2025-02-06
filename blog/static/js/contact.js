document.addEventListener('DOMContentLoaded', function() {  
    const form = document.getElementById('contactForm');
    const messageStatus = document.getElementById('message-status'); // Элемент для отображения статуса

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // предотвращаем стандартное поведение формы

        const formData = new FormData(form); // собираем данные формы
        messageStatus.style.display = 'none'; // Скрываем сообщение статуса перед отправкой

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'), // Получаем CSRF токен, если необходимо
                },
                body: formData // отправляем собранные данные
            });

            // Проверяем статус ответа
            if (response.ok) {
                messageStatus.style.display = 'block'; // Показываем сообщение об успешной отправке
                messageStatus.textContent = 'Сообщение успешно отправлено!';
                form.reset(); // очищаем форму
            } else {
                messageStatus.style.display = 'block'; // Показываем сообщение об ошибке
                messageStatus.textContent = 'Произошла ошибка при отправке сообщения.';
                messageStatus.style.color = 'red'; // Изменяем цвет на красный для ошибки
            }
        } catch (error) {
            console.error('Ошибка при отправке формы:', error);
            messageStatus.style.display = 'block';
            messageStatus.textContent = 'Произошла ошибка!';
            messageStatus.style.color = 'red'; // Для отображения ошибки
        }
    });

    // Функция для получения CSRF токена
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
