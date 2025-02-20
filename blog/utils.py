import os
import re

def count_imported_models():
    """Считает количество моделей, явно импортированных в views.py"""
    views_path = os.path.join(os.path.dirname(__file__), "views.py")  # Путь к views.py

    with open(views_path, "r", encoding="utf-8") as file:
        views_content = file.read()

    # Улучшенное регулярное выражение для учета многострочного импорта
    match = re.search(r"from \.models import \((.*?)\)", views_content, re.DOTALL)

    if match:
        models_list = re.split(r",\s*", match.group(1).replace("\n", "").strip())  # Убираем переносы строк
        return {"model_count": len(models_list), "models": models_list}
    else:
        return {"model_count": 0, "models": []}
