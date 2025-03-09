from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from blog.admin.forms import AdminUserAuthenticationForm
from blog.forms import CustomUserCreationForm, CustomUserAuthenticationForm


class AdminLoginView(FormView):
    template_name = 'admin/admin_signin.html'
    form_class = AdminUserAuthenticationForm
    success_url = reverse_lazy('admin:dashboard')

    def form_valid(self, form):
        username_or_email = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username_or_email, password=password)

        if user and (user.is_staff or user.is_superuser):
            login(self.request, user)
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid credentials or insufficient permissions.")
            return self.form_invalid(form)



@login_required(login_url='/admin/')
def admin_logout(request):
    logout(request)
    return redirect('admin_login')




class AuthView(FormView):
    template_name = "auth.html"

    def get_form_class(self):
        if self.request.path == reverse_lazy("signup"):
            return CustomUserCreationForm
        return CustomUserAuthenticationForm

    def get_success_url(self):
        if isinstance(self.get_form_class(), CustomUserCreationForm):
            return reverse_lazy("login")
        return reverse_lazy("home")

    def form_valid(self, form):
        if isinstance(form, CustomUserCreationForm):
            user = form.save()
            login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect(reverse_lazy("login"))
        else:  # Логин
            user = authenticate(
                self.request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(self.request, user)
                return redirect(reverse_lazy("home"))
            else:
                form.add_error(None, "Invalid email or password")
                return self.form_invalid(form)

        return super().form_valid(form)




def logout_view(request):
    logout(request)
    return redirect('/')

