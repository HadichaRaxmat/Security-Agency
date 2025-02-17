document.addEventListener("DOMContentLoaded", function () {
    console.log("Admin profile script initialized!");

    const editBtn = document.getElementById("edit-btn");
    const saveBtn = document.getElementById("save-btn");
    const cancelBtn = document.getElementById("cancel-btn");
    const avatarUploadContainer = document.getElementById("avatar-upload-container");
    const avatarUpload = document.getElementById("avatar-upload");
    const inputs = document.querySelectorAll(".editable");

    let originalValues = {};

    function enableEditing() {
        originalValues = {}; // Сохраняем изначальные значения

        inputs.forEach(input => {
            originalValues[input.name] = input.value;
            input.removeAttribute("readonly");
        });

        avatarUploadContainer.classList.remove("d-none");
        toggleButtons(true);
    }

    function cancelEditing() {
        inputs.forEach(input => {
            input.value = originalValues[input.name] || "";
            input.setAttribute("readonly", "true");
        });

        avatarUploadContainer.classList.add("d-none");
        toggleButtons(false);
    }

    function toggleButtons(editMode) {
        editBtn.classList.toggle("d-none", editMode);
        saveBtn.classList.toggle("d-none", !editMode);
        cancelBtn.classList.toggle("d-none", !editMode);
    }

    // Предпросмотр загружаемого аватара
    avatarUpload.addEventListener("change", function (event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                document.getElementById("avatar-preview").src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

    editBtn.addEventListener("click", enableEditing);
    cancelBtn.addEventListener("click", cancelEditing);

    function goBackOrDashboard() {
        if (document.referrer) {
            window.history.back(); // Если есть предыдущая страница, вернуться назад
        } else {
            window.location.href = "/dashboard"; // Если нет — отправить на Dashboard
        }
    }

});

