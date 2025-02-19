if (typeof $ === "undefined") {
    console.error("❌ jQuery не загружен! Проверь порядок подключения скриптов.");
} else {
    console.log("✅ jQuery загружен корректно.");
}
$(document).ready(function() {
    if (typeof jQuery === 'undefined') {
        console.error("⚠️ jQuery не загружен! Проверь подключение.");
        return;
    }
    if (!$.fn.DataTable) {
        console.error("⚠️ DataTables не загружен!");
        return;
    }

    console.log("✅ Инициализируем DataTables...");

    $('#headersTable').DataTable({
        dom: 'Bfrtip',
        buttons: ['copy', 'csv', 'excel', 'pdf', 'print'],
        lengthMenu: [10, 25, 50, 100],
        pageLength: 5, // По умолчанию 25 строк
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.11.5/i18n/en-GB.json"
        }
    });
});

console.log("✅ jQuery загружен?", typeof $ !== 'undefined');