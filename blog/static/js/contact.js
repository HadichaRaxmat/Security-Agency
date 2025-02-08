document.addEventListener('DOMContentLoaded', function() {  
    const form = document.getElementById('contactForm');
    const flashMessage = document.getElementById('flash-message'); // Элемент для отображения статуса

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // предотвращаем стандартное поведение формы

        const formData = new FormData(form); // собираем данные формы

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: formData
            });

            if (response.ok) {
                showFlashMessage('Сообщение успешно отправлено!', 'green');
                form.reset(); // очищаем форму
            } else {
                showFlashMessage('Ошибка при отправке сообщения!', 'red');
            }
        } catch (error) {
            console.error('Ошибка при отправке формы:', error);
            showFlashMessage('Произошла ошибка!', 'red');
        }
    });

    function showFlashMessage(text) {
        flashMessage.textContent = text;
        flashMessage.style.color = 'white'; // Белый текст
        flashMessage.style.backgroundColor = 'transparent'; // Прозрачный фон
        flashMessage.style.display = 'block';

        setTimeout(() => {
            flashMessage.classList.add('hide');
        }, 3000);

        setTimeout(() => {
            flashMessage.style.display = 'none';
            flashMessage.classList.remove('hide');
        }, 3500);
    }


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
