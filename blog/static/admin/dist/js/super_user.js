document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".delete-admin-btn").forEach(button => {
        button.addEventListener("click", function (event) {
            event.preventDefault();  // Остановим стандартное действие

            let userId = this.getAttribute("data-user-id");  // Получаем ID из кнопки
            let userRole = this.getAttribute("data-user-role");  // Получаем роль

            if (userRole === "superuser") {
                alert("❌ Суперпользователь не может быть удалён!");
                return;  // Останавливаем выполнение
            }

            let confirmDelete = confirm("Вы уверены, что хотите удалить этого пользователя?");
            if (confirmDelete) {
                window.location.href = this.getAttribute("href");  // Перенаправляем на удаление
            }
        });
    });
});
