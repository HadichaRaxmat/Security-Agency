from blog.admin.forms import AdminProfileUpdateForm, AvatarUpdateForm


class AdminService:

    @staticmethod
    def get_profile_form(user):
        return AdminProfileUpdateForm if user.is_superuser else AvatarUpdateForm

    @staticmethod
    def update_profile(user, form):
        form.save()

    @staticmethod
    def create_admin(form, role):
        user = form.save(commit=False)
        user.is_staff = True
        user.is_admin = True

        if role not in ['admin', 'moderator', 'editor', 'support', 'admin_manager']:
            return None
        user.role = role
        user.save()
        return user
