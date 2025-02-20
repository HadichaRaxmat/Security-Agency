from django.contrib.auth import get_user_model
from django.apps import apps
from datetime import timedelta
from django.utils.timezone import now
from django.urls import reverse
CustomUser = get_user_model()
from .models import CustomUser, UserContact

def user_count(request):
    return {'user_count': CustomUser.objects.filter(is_staff=False, is_superuser=False).count()}


from .utils import count_imported_models

def model_count(request):
    return count_imported_models()



def global_context(request):
    model_names = [
        "Header", "ContactUs", "Menu", "Slider", "About", "ServiceHeader",
        "Service", "Client", "Touch", "Team", "Guard", "Info", "Subscribe", "Footer"
    ]

    context = {model_name.lower(): apps.get_model("blog", model_name).objects.all() for model_name in model_names}
    context["contact_url"] = reverse("contact")
    context["current_url"] = request.path

    return context


def active_users_count(request):
    last_24_hours = now() - timedelta(hours=24)
    active_users = CustomUser.objects.filter(last_login__gte=last_24_hours, is_staff=False, is_superuser=False).count()
    return {'active_users': active_users}



def completed_requests_percentage(request):
    total_users = CustomUser.objects.filter(is_staff=False, is_superuser=False).count()
    total_requests = UserContact.objects.count()

    percentage = (total_requests / total_users * 100) if total_users > 0 else 0
    return {'completed_requests_percentage': round(percentage, 1)}


def notifications(request):
    unread_count = UserContact.objects.filter(status='unread').count()
    unread_contacts = UserContact.objects.filter(status='unread')

    return {
        'unread_count': unread_count,
        'unread_contacts': unread_contacts
    }