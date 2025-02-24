import os
import re

def count_imported_models():
    """Считает количество моделей, импортированных в admin_views.py"""
    views_path = os.path.join(os.path.dirname(__file__), "admin", "admin_views.py")

    print(f"Checking file: {views_path}")

    with open(views_path, "r", encoding="utf-8") as file:
        views_content = file.read()

    matches = re.findall(r"from\s+[\w\.]+models\s+import\s+\((.*?)\)", views_content, re.DOTALL)

    if matches:
        models_list = []
        for match in matches:
            cleaned_models = match.replace("\n", "").strip()
            models_list.extend(re.split(r",\s*", cleaned_models))

        print(f"Found models: {models_list}")
        return {"model_count": len(models_list), "models": models_list}
    else:
        print("No models found")  # Отладка
        return {"model_count": 0, "models": []}
