from django.contrib.auth import get_user_model
from django.apps import apps
from django.urls import reverse
CustomUser = get_user_model()

def user_count(request):
    return {'user_count': CustomUser.objects.count()}



def global_context(request):
    model_names = [
        "Header", "ContactUs", "Menu", "Slider", "About", "ServiceHeader",
        "Service", "Client", "Touch", "Team", "Guard", "Info", "Subscribe", "Footer"
    ]

    context = {model_name.lower(): apps.get_model("blog", model_name).objects.all() for model_name in model_names}
    context["contact_url"] = reverse("contact")
    context["current_url"] = request.path

    return context