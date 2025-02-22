from django.contrib import messages
from django.shortcuts import get_object_or_404
from blog.models import CustomUser
from blog.forms import UserContactForm


class UserService:

    @staticmethod
    def get_users_list():
        return CustomUser.objects.filter(is_staff=False, is_superuser=False)

    @staticmethod
    def update_user(user, form):
        form.save()
        return user

    @staticmethod
    def delete_user(user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        return True

