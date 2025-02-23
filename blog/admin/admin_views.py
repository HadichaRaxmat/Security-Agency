from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from blog.admin.forms import AdminUserCreationForm, AdminUserUpdateForm
from blog.services.admin_service import AdminService
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog.forms import (HeaderForm, MenuForm, SliderForm, AboutForm, ServiceHeaderForm, ServiceForm, ClientForm,
                        TouchForm,
                        TeamForm, GuardForm, InfoForm, ContactUsForm, SubscribeForm, FooterForm, UserContactForm,
                        CustomUserCreationForm, CustomUserUpdateForm)
from blog.models import (Header, Menu, Slider, About, ServiceHeader, Service, Client, Touch, Team, Guard, Info,
                         ContactUs,
                         Subscribe, Footer, UserContact, CustomUser)



@login_required(login_url='/admin/')
def admin_view(request):
    return render(request, 'admin/index.html')


class AdminProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'admin/admin_profile.html'
    success_url = reverse_lazy('admin:admin_profile')

    def get_object(self):
        return self.request.user

    def get_form_class(self):
        return AdminService.get_profile_form(self.request.user)

    def form_valid(self, form):
        AdminService.update_profile(self.request.user, form)
        messages.success(self.request, "Профиль успешно обновлён!")
        return super().form_valid(form)


class AdminListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'admin/admin_list.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        return CustomUser.objects.filter(is_staff=True)


class AdminCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    form_class = AdminUserCreationForm
    template_name = 'admin/admin_create.html'
    success_url = reverse_lazy('admin:admin_list')

    def test_func(self):
        return self.request.user.role in ['superuser', 'admin_manager']

    def form_valid(self, form):
        role = self.request.POST.get('role', 'admin')
        user = AdminService.create_admin(form, role)

        if not user:
            messages.error(self.request, "You do not have permission to assign this role.")
            return self.form_invalid(form)

        messages.success(self.request, f"Admin {user.email} ({user.get_role_display()}) created successfully.")
        return super().form_valid(form)


class AdminUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = AdminUserUpdateForm
    template_name = 'admin/admin_update.html'
    success_url = reverse_lazy('admin:admin_list')

    def test_func(self):
        return self.request.user.is_superuser

    def get_object(self):
        return get_object_or_404(CustomUser, id=self.kwargs['user_id'])

    def form_valid(self, form):
        messages.success(self.request, "Admin details updated successfully.")
        return super().form_valid(form)


class AdminDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'admin/admin_delete.html'
    success_url = reverse_lazy('admin:admin_list')
    login_url = '/admin/'

    def test_func(self):
        return self.request.user.is_superuser

    def get_object(self):
        return get_object_or_404(CustomUser, id=self.kwargs['user_id'])




class UsersListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'admin/users.html'
    context_object_name = 'users'
    login_url = '/admin/'

    def get_queryset(self):
        return CustomUser.objects.filter(is_staff=False, is_superuser=False)



class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm  # Используем форму для обновления
    template_name = 'admin/user_update.html'
    success_url = reverse_lazy('admin:user_list')
    login_url = '/admin/'





class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'admin/user_delete.html'
    success_url = reverse_lazy('admin:user_list')
    login_url = '/admin/'



class HeaderListView(ListView):
    model = Header
    template_name = 'admin/header_list.html'
    context_object_name = 'headers'


class HeaderCreateView(CreateView):
    model = Header
    form_class = HeaderForm
    template_name = 'admin/header_create.html'
    success_url = reverse_lazy('admin:header_list')


class HeaderUpdateView(UpdateView):
    model = Header
    form_class = HeaderForm
    template_name = 'admin/header_update.html'
    success_url = reverse_lazy('admin:header_list')


class HeaderDeleteView(LoginRequiredMixin, DeleteView):
    model = Header
    template_name = 'admin/header_delete.html'
    success_url = reverse_lazy('admin:header_list')
    login_url = '/admin/'


class MenuListView(ListView):
    model = Menu
    template_name = 'admin/menu_list.html'
    context_object_name = 'menu'


class MenuAddView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'admin/menu_add.html'
    success_url = reverse_lazy('admin:menu_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.get_url()
        return response


class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'admin/menu_create.html'
    success_url = reverse_lazy('admin:menu_list')


class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'admin/menu_delete.html'
    success_url = reverse_lazy('admin:admin_list')


def menu_toggle_visibility(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    menu.is_active = not menu.is_active
    menu.save()
    return redirect('menu_list')


class SliderCreateView(CreateView):
    model = Slider
    form_class = SliderForm
    template_name = 'admin/slider_create.html'
    success_url = reverse_lazy('admin:slider_list')


class SliderListView(ListView):
    model = Slider
    template_name = 'admin/slider_list.html'
    context_object_name = 'sliders'


class SliderUpdateView(UpdateView):
    model = Slider
    form_class = SliderForm
    template_name = 'admin/slider_update.html'
    success_url = reverse_lazy('admin:slider_list')


class SliderDeleteView(DeleteView):
    model = Slider
    template_name = 'admin/slider_delete.html'
    success_url = reverse_lazy('slider_list')


class AboutCreateView(CreateView):
    model = About
    form_class = AboutForm
    template_name = 'admin/about_create.html'
    success_url = reverse_lazy('admin:about_list')


class AboutListView(ListView):
    model = About
    template_name = 'admin/about_list.html'
    context_object_name = 'abouts'


class AboutUpdateView(UpdateView):
    model = About
    form_class = AboutForm
    template_name = 'admin/about_update.html'
    success_url = reverse_lazy('admin:about_list')


class AboutDeleteView(DeleteView):
    model = About
    template_name = 'admin/about_delete.html'
    success_url = reverse_lazy('admin:about_list')


class ServiceHeaderCreateView(LoginRequiredMixin, CreateView):
    model = ServiceHeader
    form_class = ServiceHeaderForm
    template_name = 'admin/service_header_create.html'
    success_url = reverse_lazy('admin:service_header_list')
    login_url = '/admin/'


class ServiceHeaderListView(LoginRequiredMixin, ListView):
    model = ServiceHeader
    template_name = 'admin/service_header_list.html'
    context_object_name = 'service_headers'
    login_url = '/admin/'


class ServiceHeaderUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceHeader
    form_class = ServiceHeaderForm
    template_name = 'admin/service_header_update.html'
    success_url = reverse_lazy('admin:service_header_list')
    login_url = '/admin/'


class ServiceHeaderDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceHeader
    template_name = 'admin/service_header_delete.html'
    success_url = reverse_lazy('admin:servie_header_list')
    login_url = '/admin/'


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'admin/service_create.html'
    success_url = reverse_lazy('admin:service_list')
    login_url = '/admin/'


class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    template_name = 'admin/service_list.html'
    context_object_name = 'services'
    login_url = '/admin/'


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'admin/service_update.html'
    success_url = reverse_lazy('admin:service_list')
    login_url = '/admin/'


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = 'admin/service_delete.html'
    success_url = reverse_lazy('admin:service_list')
    login_url = '/admin/'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'admin/client_create.html'
    success_url = reverse_lazy('client_list')
    login_url = '/admin/'


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'admin/client_list.html'
    context_object_name = 'clients'
    login_url = '/admin/'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'admin/client_update.html'
    success_url = reverse_lazy('admin:client_list')
    login_url = '/admin/'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'admin/client_delete.html'
    success_url = reverse_lazy('admin:client_list')
    login_url = '/admin/'


class TouchCreateView(LoginRequiredMixin, CreateView):
    model = Touch
    form_class = TouchForm
    template_name = 'admin/touch_create.html'
    success_url = reverse_lazy('admin:touch_list')


class TouchListView(LoginRequiredMixin, ListView):
    model = Touch
    template_name = 'admin/touch_list.html'
    context_object_name = 'touches'
    login_url = '/admin/'


class TouchUpdateVIew(LoginRequiredMixin, UpdateView):
    model = Touch
    form_class = TouchForm
    template_name = 'admin/touch_update.html'
    success_url = reverse_lazy('admin:touch_list')
    login_url = '/admin/'


class TouchDeleteView(LoginRequiredMixin, DeleteView):
    model = Touch
    template_name = 'admin/touch_delete.html'
    success_url = reverse_lazy('admin:touch_list')
    login_url = '/admin/'


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'admin/team_create.html'
    success_url = reverse_lazy('admin:team_list')
    login_url = '/admin/'


class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'admin/team_list.html'
    context_object_name = 'teams'
    login_url = '/admin/'


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'admin/team_update.html'
    success_url = reverse_lazy('admin:team_list')
    login_url = '/admin/'


class TeamDeleteVIew(LoginRequiredMixin, DeleteView):
    model = Team
    template_name = 'admin/team_delete.html'
    success_url = reverse_lazy('admin:team_list')
    login_url = '/admin/'


class GuardCreateView(LoginRequiredMixin, CreateView):
    model = Guard
    form_class = GuardForm
    template_name = 'admin/guard_create.html'
    success_url = reverse_lazy('admin:guard_list')
    login_url = '/admin/'


class GuardListView(LoginRequiredMixin, ListView):
    model = Guard
    template_name = 'admin/guard_list.html'
    context_object_name = 'guards'
    login_url = '/admin/'


class GuardUpdateView(LoginRequiredMixin, UpdateView):
    model = Guard
    form_class = GuardForm
    template_name = 'admin/guard_update.html'
    success_url = reverse_lazy('admin:guard_list')
    login_url = '/admin/'


class GuardDeleteView(LoginRequiredMixin, DeleteView):
    model = Guard
    template_name = 'admin/guard_delete.html'
    success_url = reverse_lazy('admin:guard_list')
    login_url = '/admin/'


class InfoCreateView(LoginRequiredMixin, CreateView):
    model = Info
    form_class = InfoForm
    template_name = 'admin/info_create.html'
    success_url = reverse_lazy('admin:info_list')
    login_url = '/admin/'


class InfoListView(LoginRequiredMixin, ListView):
    model = Info
    template_name = 'admin/info_list.html'
    context_object_name = 'infos'
    login_url = '/admin/'


class InfoUpdateView(LoginRequiredMixin, UpdateView):
    model = Info
    form_class = InfoForm
    template_name = 'admin/info_update.html'
    success_url = reverse_lazy('admin:info_list')
    login_url = '/admin/'


class InfoDeleteView(LoginRequiredMixin, DeleteView):
    model = Info
    template_name = 'admin/info_delete.html'
    success_url = reverse_lazy('admin:info_list')
    login_url = '/admin/'


class ContactusCreateView(LoginRequiredMixin, CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'admin/contact_us_create.html'
    success_url = reverse_lazy('admin:contactus_list')
    login_url = '/admin/'


class ContactusListView(LoginRequiredMixin, ListView):
    model = ContactUs
    template_name = 'admin/contact_us_list.html'
    context_object_name = 'contactus_entries'
    login_url = '/admin/'


class ContactusUpdateView(LoginRequiredMixin, UpdateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'admin/contact_us_update.html'
    success_url = reverse_lazy('admin:contactus_list')
    login_url = '/admin/'


class ContactusDeleteView(LoginRequiredMixin, DeleteView):
    model = ContactUs
    template_name = 'admin/contact_us_delete'
    success_url = reverse_lazy('admin:contactus_list')
    login_url = '/admin/'


class SubscribeCreateView(LoginRequiredMixin, CreateView):
    model = Subscribe
    form_class = SubscribeForm
    template_name = 'admin/subscribe_create'
    success_url = reverse_lazy('admin:subscribe_list')
    login_url = '/admin/'


class SubscribeListView(LoginRequiredMixin, ListView):
    model = Subscribe
    template_name = 'admin/subscribe_list.html'
    context_object_name = 'subscribes'
    login_url = '/admin/'


class SubscribeUpdateView(LoginRequiredMixin, UpdateView):
    model = Subscribe
    form_class = SubscribeForm
    template_name = 'admin/subscribe_update.html'
    success_url = reverse_lazy('admin:subscribe_list')
    login_url = '/admin/'


class SubscribeDeleteView(LoginRequiredMixin, DeleteView):
    model = Subscribe
    template_name = 'admin/subscribe_delete.html'
    success_url = reverse_lazy('admin:subscribe_list')
    login_url = '/admin/'


class FooterCreateView(LoginRequiredMixin, CreateView):
    model = Footer
    form_class = FooterForm
    template_name = 'admin/footer_create.html'
    success_url = reverse_lazy('admin:subscribe_list')
    login_url = '/admin/'


class FooterListView(LoginRequiredMixin, ListView):
    model = Footer
    template_name = 'admin/footer_list.html'
    context_object_name = 'footers'
    login_url = '/admin/'


class FooterUpdateView(LoginRequiredMixin, UpdateView):
    model = Footer
    form_class = FooterForm
    template_name = 'admin/footer_update.html'
    success_url = reverse_lazy('admin:footer_list')
    login_url = '/admin/'


class FooterDeleteView(LoginRequiredMixin, DeleteView):
    model = Footer
    template_name = 'admin/footer_delete.html'
    success_url = reverse_lazy('admin:footer_list')
    login_url = '/admin/'


@login_required(login_url='/admin/')
def footer_bulk_delete(request):
    if request.method == 'POST':
        selected_footers = request.POST.getlist('selected_footers')
        if selected_footers:
            Footer.objects.filter(id__in=selected_footers).delete()
            messages.success(request, 'Selected footers deleted successfully!')
        else:
            messages.error(request, 'No footers selected for deletion.')

    return redirect('footer_list')


class UserContactCreateView(LoginRequiredMixin, CreateView):
    model = UserContact
    form_class = UserContactForm
    template_name = 'admin/user_contact_create'
    success_url = reverse_lazy('admin:user_contact_list')
    login_url = '/admin/'


def mark_as_read(request, contact_id):
    contact = get_object_or_404(UserContact, id=contact_id)
    contact.status = 'read'
    contact.save()
    return redirect('admin:user_contact_list')


class UserContactListView(LoginRequiredMixin, ListView):
    model = UserContact
    template_name = 'admin/user_contact_list.html'
    context_object_name = 'user_contacts'
    login_url = '/admin/'


class UserContactUpdateView(LoginRequiredMixin, UpdateView):
    model = UserContact
    form_class = UserContactForm
    template_name = 'admin/user_contact_update.html'
    success_url = reverse_lazy('admin:user_contact_list')
    login_url = '/admin/'


class UserContactDeleteView(LoginRequiredMixin, DeleteView):
    model = UserContact
    form_class = UserContactForm
    template_name = 'admin/user_contact_update.html'
    success_url = reverse_lazy('admin:user_contact_list')
    login_url = '/admin/'
