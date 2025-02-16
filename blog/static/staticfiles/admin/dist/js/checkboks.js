document.addEventListener("DOMContentLoaded", function() {
    const selectAllCheckbox = document.getElementById('select-all');
    const footerCheckboxes = document.querySelectorAll('.footer-checkbox');
    const bulkDeleteButton = document.getElementById('bulk-delete-btn');

    // Функция для включения/выключения кнопки удаления
    function toggleBulkDeleteButton() {
        const selectedFooters = document.querySelectorAll('.footer-checkbox:checked').length;
        bulkDeleteButton.disabled = selectedFooters === 0;
    }

    // Выбор всех чекбоксов
    selectAllCheckbox.addEventListener('change', function() {
        footerCheckboxes.forEach(checkbox => {
            checkbox.checked = selectAllCheckbox.checked;
        });
        toggleBulkDeleteButton();
    });

    // Отслеживание изменения состояния чекбоксов
    footerCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', toggleBulkDeleteButton);
    });

    // Отключаем кнопку удаления, если ничего не выбрано
    toggleBulkDeleteButton();
});
