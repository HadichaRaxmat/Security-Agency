$(document).ready(function() {
    console.log("jQuery загружен:", typeof $ !== "undefined");
    console.log("DataTables загружен:", typeof $.fn.DataTable !== "undefined");

    if (typeof $.fn.DataTable === "undefined") {
        console.error("Ошибка: DataTables не загрузился!");
        return;
    }

    $('#headersTable').DataTable({
        "paging": true,
        "searching": true,
        "ordering": true,
        "info": true,
        "lengthMenu": [5, 10, 25, 50],
        "language": {
            "lengthMenu": "Показать _MENU_ записей",
            "search": "Поиск:",
            "info": "Показано _START_ - _END_ из _TOTAL_ записей",
            "paginate": {
                "first": "Первая",
                "last": "Последняя",
                "next": "→",
                "previous": "←"
            }
        }
    });

    console.log("DataTables успешно инициализирован!");
});


console.log(typeof $.fn.DataTable);
