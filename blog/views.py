from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse_lazy
from django.views.generic import FormView
CustomUser = get_user_model()
from .forms import UserContactForm



def home_view(request):
    return render(request, "index.html")

def about_view(request):
    return render(request, "about.html")

def service_view(request):
    return render(request, "service.html")

def guard_view(request):
    return render(request, "guard.html")


def contact_view(request):
    return render(request, 'contact.html')



class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = UserContactForm
    success_url = reverse_lazy("/")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ваше сообщение успешно отправлено!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка! Проверьте введённые данные.")
        return super().form_invalid(form)



