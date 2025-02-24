from django.http import Http404

from blog.admin.forms import AdminProfileUpdateForm, AvatarUpdateForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
User = get_user_model()

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
    def delete_admin(current_user, user_id):
        """Удаляет администратора, если у текущего пользователя есть права."""
        from blog.models import CustomUser  # Избегаем циклического импорта

        try:
            user_to_delete = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise Http404("Пользователь не найден.")

        # 🚨 1. Полный запрет на удаление суперпользователя
        if user_to_delete.is_superuser:
            raise PermissionDenied("❌ Нельзя удалить суперпользователя!")

        # 🚨 2. Запрещаем удалять себя
        if current_user == user_to_delete:
            raise PermissionDenied("❌ Вы не можете удалить самого себя!")

        # ✅ 3. Разрешаем удаление только суперпользователю
        if not current_user.is_superuser:
            raise PermissionDenied("❌ Только суперпользователь может удалять администраторов.")

        # ✅ 4. Удаление разрешено
        user_to_delete.delete()
        return True
