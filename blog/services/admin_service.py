from django.http import Http404

from blog.admin.forms import AdminProfileUpdateForm, AvatarUpdateForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib import messages


class AdminService:

    @staticmethod
    def get_profile_form(user):
        return AdminProfileUpdateForm if user.is_superuser else AvatarUpdateForm

    @staticmethod
    def update_profile(user, form):
        form.save()

    @staticmethod
    def create_admin(request_user, form, role):
        if not request_user.is_superuser:
            raise PermissionDenied("Только суперпользователь может создавать администраторов.")

        if role not in ['admin', 'moderator', 'editor', 'support', 'admin_manager']:
            return None

        user = form.save(commit=False)
        user.is_staff = True
        user.is_admin = True
        user.role = role
        user.save()
        return user

    @staticmethod
    def delete_admin(request, request_user, user_id):
        from blog.models import CustomUser

        try:
            user_to_delete = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            messages.error(request, "❌ Пользователь не найден.")
            print("⛔ Ошибка: Пользователь не найден")
            return False

        print(f"🔍 Проверка: {user_to_delete.email} (is_superuser={user_to_delete.is_superuser})")

        if user_to_delete.is_superuser:
            messages.error(request, "❌ Нельзя удалить суперпользователя!")
            print("⛔ Попытка удалить суперпользователя! Операция запрещена.")
            return False

        if request_user == user_to_delete:
            messages.error(request, "❌ Вы не можете удалить самого себя!")
            print("⛔ Пользователь пытался удалить сам себя")
            return False

        if not request_user.is_superuser:
            messages.error(request, "❌ Только суперпользователь может удалять администраторов.")
            print("⛔ Обычный администратор пытался удалить другого администратора")
            return False

        print(f"✅ Удаление разрешено: {user_to_delete.email}")
        user_to_delete.delete()
        messages.success(request, f"✅ Администратор {user_to_delete.email} удалён.")
        return True
