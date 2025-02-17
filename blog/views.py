from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserContactSerializer
from rest_framework.permissions import AllowAny

CustomUser = get_user_model()
from .models import Header, Menu, Slider, About, ServiceHeader, Service, Client, Touch, Team, Guard, Info, ContactUs, \
    Subscribe, Footer, UserContact, CustomUser, HeaderTouch
from .forms import (HeaderForm, MenuForm, SliderForm, AboutForm, ServiceHeaderForm, ServiceForm, ClientForm, TouchForm, \
                    TeamForm, GuardForm, InfoForm, ContactUsForm, SubscribeForm, FooterForm, UserContactForm,
                    AdminUserCreationForm,
                    CustomUserCreationUserForm, AdminUserAuthenticationForm, CustomAuthenticationForm,
                    AdminUserUpdateForm,
                    AvatarUpdateForm, AdminProfileUpdateForm)


def home_view(request):
    header = Header.objects.all()
    contactus = ContactUs.objects.all()
    slider = Slider.objects.all()
    about = About.objects.all()
    serviceh = ServiceHeader.objects.all()
    service = Service.objects.all()
    client = Client.objects.all()
    touch = Touch.objects.all()
    team = Team.objects.all()
    guard = Guard.objects.all()
    contact_url = reverse('contact')
    info = Info.objects.all()
    subscribe = Subscribe.objects.all()
    footer = Footer.objects.all()
    menu = Menu.objects.all()
    current_url = request.path
    d = {
        'header': header,
        'contactus': contactus,
        'menu': menu,
        'slider': slider,
        'about': about,
        'serviceh': serviceh,
        'service': service,
        'client': client,
        'touch': touch,
        'team': team,
        'guard': guard,
        'contact_url': contact_url,
        'info': info,
        'subscribe': subscribe,
        'footer': footer,
        'current_url': current_url,
    }
    return render(request, 'index.html', context=d)


def about_view(request):
    header = Header.objects.all()
    contactus = ContactUs.objects.all()
    menu = Menu.objects.all()
    about = About.objects.all()
    info = Info.objects.all()
    subscribe = Subscribe.objects.all()
    footer = Footer.objects.all()
    d = {
        'header': header,
        'contactus': contactus,
        'menu': menu,
        'about': about,
        'info': info,
        'subscribe': subscribe,
        'footer': footer

    }
    return render(request, 'about.html', context=d)


def service_view(request):
    header = Header.objects.all()
    contactus = ContactUs.objects.all()
    menu = Menu.objects.all()
    slider = Slider.objects.all()
    about = About.objects.all()
    serviceh = ServiceHeader.objects.all()
    service = Service.objects.all()
    footer = Footer.objects.all()
    info = Info.objects.all()
    subscribe = Subscribe.objects.all()
    d = {
        'header': header,
        'contactus': contactus,
        'menu': menu,
        'slider': slider,
        'about': about,
        'serviceh': serviceh,
        'service': service,
        'footer': footer,
        'info': info,
        'subscribe': subscribe

    }
    return render(request, 'service.html', context=d)


def guard_view(request):
    header = Header.objects.all()
    contactus = ContactUs.objects.all()
    menu = Menu.objects.all()
    slider = Slider.objects.all()
    about = About.objects.all()
    footer = Footer.objects.all()
    info = Info.objects.all()
    subscribe = Subscribe.objects.all()
    team = Team.objects.all()
    guard = Guard.objects.all()
    current_url = request.path,
    d = {
        'header': header,
        'contactus': contactus,
        'menu': menu,
        'slider': slider,
        'about': about,
        'current_url': current_url,
        'footer': footer,
        'info': info,
        'subscribe': subscribe,
        'team': team,
        'guard': guard,

    }
    return render(request, 'guard.html', context=d)


def contact_view(request):
    login_errors = None
    register_errors = None

    if request.method == 'POST':
        data = request.POST

        # 1. ЛОГИН
        if 'login_form' in data:
            form = CustomAuthenticationForm(data=request.POST)
            if form.is_valid():
                user = authenticate(
                    request,
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
                if user:
                    login(request, user)
                    return redirect('contact')
                else:
                    login_errors = "Неверный email или пароль"
            else:
                login_errors = "Ошибка входа. Проверьте данные."

        # 2. РЕГИСТРАЦИЯ
        elif 'register_form' in data:
            form = CustomUserCreationUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Добавил backend
                return redirect('contact')
            else:
                register_errors = "Ошибка регистрации. Проверьте данные."  # Теперь ошибки отображаются аналогично логину

        # 3. ФОРМА ОБРАТНОЙ СВЯЗИ
        else:
            UserContact.objects.create(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                message=data['message']
            )
            return redirect('/')

    footer = Footer.objects.all()
    header = Header.objects.all()
    contactus = ContactUs.objects.all()
    menu = Menu.objects.all()
    info = Info.objects.all()
    subscribe = Subscribe.objects.all()
    current_url = request.path

    d = {
        'header': header,
        'contactus': contactus,
        'menu': menu,
        'info': info,
        'subscribe': subscribe,
        'current_url': current_url,
        'footer': footer,
        'login_errors': login_errors,
        'register_errors': register_errors,
        'form': CustomUserCreationUserForm(),  # Добавил форму регистрации
        'login_form': CustomAuthenticationForm()  # Добавил форму логина
    }

    return render(request, 'contact.html', context=d)


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user,
                  backend='django.contrib.auth.backends.ModelBackend')

            return redirect('login')
    else:
        form = CustomUserCreationUserForm()
    return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'signin.html', {'form': form})


@login_required(login_url='/admin/')
def admin_view(request):
    return render(request, 'admin/index.html')


@login_required(login_url='/admin/')
def admin_profile(request):
    profile = request.user

    if request.method == "POST":
        if request.user.is_superuser:
            form = AdminProfileUpdateForm(request.POST, request.FILES, instance=profile)
        else:
            form = AvatarUpdateForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлён!")
            return redirect("admin_profile")

    else:
        form = AdminProfileUpdateForm(instance=profile) if request.user.is_superuser else AvatarUpdateForm(
            instance=profile)

    return render(request, 'admin/admin_profile.html', {'form': form})


@login_required(login_url='/admin/')
def admin_list(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    users = CustomUser.objects.filter(is_staff=True)
    return render(request, 'admin/admin_list.html', {'users': users})


@login_required(login_url='/admin/')
def admin_create(request):
    print(f"Superuser: {request.user.is_superuser}, Role: {getattr(request.user, 'role', 'No role')}")

    if request.user.role not in ['superuser', 'admin_manager']:
        messages.error(request, "You do not have permission to create an admin.")
        return redirect('dashboard')

    if request.method == "POST":
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_admin = True
            user.save()

            allowed_roles = ['admin', 'moderator', 'editor', 'support']
            if request.user.role == 'superuser':
                allowed_roles.append('admin_manager')

            role = request.POST.get('role', 'admin')
            if role not in allowed_roles:
                messages.error(request, "You do not have permission to assign this role.")
                return redirect('admin_create')

            user.role = role
            user.save()
            messages.success(request, f"Admin {user.email} ({user.get_role_display()}) created successfully.")
            return redirect('admin_list')

    else:
        form = AdminUserCreationForm()

    return render(request, 'admin/admin_create.html', {'form': form})


@login_required(login_url='/admin/')
def admin_update(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, is_admin=True)

    if not request.user.is_superuser:
        return JsonResponse({"error": "You are not authorized to edit admin users."}, status=403)

    if request.method == 'POST':
        form = AdminUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": "Admin details updated successfully.", "redirect": "/admin/list/"})

    else:
        form = AdminUserUpdateForm(instance=user)

    return render(request, 'admin/admin_update.html', {'form': form, 'user': user})


@login_required(login_url='/admin/')
def admin_delete(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, is_admin=True)

    if not request.user.is_superuser:
        return JsonResponse({"error": "You are not authorized to delete admin users."}, status=403)

    if request.method == 'POST':
        user.delete()
        return JsonResponse({"success": "Admin user deleted successfully.", "redirect": "/admin/list/"})

    return render(request, 'admin/admin_delete.html', {'user': user})


def admin_login(request):
    form = AdminUserAuthenticationForm(data=request.POST or None)
    if form.is_valid():
        username_or_email = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username_or_email, password=password)
        if user and (user.is_staff or user.is_superuser):
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials or insufficient permissions.")

    return render(request, 'admin/admin_signin.html', {'form': form})


@login_required(login_url='/admin/')
def admin_logout(request):
    logout(request)
    return redirect('admin_login')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/admin/')
def users_list(request):
    users = CustomUser.objects.filter(is_staff=False, is_superuser=False)
    return render(request, 'admin/users.html', {'users': users})


def user_update(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    if request.method == 'POST':
        form = CustomUserCreationUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = CustomUserCreationUserForm(instance=user)
    return render(request, 'admin/user_update.html', {'form': form, 'user': user})


def user_delete(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    return render(request, 'admin/user_delete.html', {'user': user})


def header_create(request):
    if request.method == 'POST':
        form = HeaderForm(request.POST, request.FILES)
        if form.is_valid():
            if Header.objects.exists():
                form.add_error('logo', 'Только один логотип может быть добавлен.')
                return render(request, 'admin/header_create.html', {'form': form})
            form.save()
            return redirect('header_list')
    else:
        form = HeaderForm()
    return render(request, 'admin/header_create.html', {'form': form})


def header_list(request):
    header = Header.objects.all()
    return render(request, 'admin/header_list.html', {'header': header})


def header_update(request, pk):
    header = get_object_or_404(Header, id=pk)
    if request.method == 'POST':
        form = HeaderForm(request.POST, instance=header)
        if form.is_valid():
            form.save()
            return redirect('header_list')
    else:
        form = HeaderForm(instance=header)
    return render(request, 'admin/header_update.html', {'form': form, 'header': header})


def header_delete(request, pk):
    header = get_object_or_404(Header, id=pk)

    if request.method == 'POST':
        header.delete()
        return redirect('header_list')
    return render(request, 'admin/header_delete.html', {'header': header})


def menu_list(request):
    menu = Menu.objects.all()
    return render(request, 'admin/menu_list.html', {'menu': menu})


def menu_add(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu_instance = form.save()
            menu_instance.get_url()
            return redirect("menu_list")
    else:
        form = MenuForm()
        print(form)
    return render(request, "admin/menu_add.html", {"form": form})


def menu_update(request, pk):
    menu = get_object_or_404(Menu, id=pk)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.errors:
            return render(request, "admin/menu_update.html", {'text': form.errors})
        form.save()
        return redirect("menu_list")

    else:
        form = MenuForm(instance=menu)

    return render(request, "admin/menu_update.html", {"form": form, 'menu': menu})


def menu_delete(request, pk):
    menu = get_object_or_404(Menu, id=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, 'admin/menu_delete.html', {'menu': menu})


def menu_toggle_visibility(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    menu.is_active = not menu.is_active
    menu.save()
    return redirect('menu_list')


def slider_create(request):
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('slider_list')
    else:
        form = SliderForm()
    return render(request, 'admin/slider_create.html', {'form': form})


def slider_list(request):
    sliders = Slider.objects.all()
    return render(request, 'admin/slider_list.html', {'sliders': sliders})


def slider_update(request, pk):
    slider = get_object_or_404(Slider, id=pk)
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=slider)
        if form.is_valid():
            form.save()
            return redirect('slider_list')
    else:
        form = SliderForm(instance=slider)
    return render(request, 'admin/slider_update.html', {'form': form, 'slider': slider})


def slider_delete(request, pk):
    slider = get_object_or_404(Slider, id=pk)
    if request.method == 'POST':
        slider.delete()
        return redirect('slider_list')
    return render(request, 'admin/slider_delete.html', {'slider': slider})


def about_create(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about_list')  # редирект на страницу со списком
        else:
            print(form.errors)  # Вывод ошибок формы для отладки
    else:
        form = AboutForm()

    return render(request, 'admin/about_create.html', {'form': form})


def about_list(request):
    abouts = About.objects.all()
    return render(request, 'admin/about_list.html', {'abouts': abouts})


def about_update(request, pk):
    about = get_object_or_404(About, id=pk)
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about_list')
    else:
        form = AboutForm(instance=about)
    return render(request, 'admin/about_update.html', {'form': form, 'about': about})


def about_delete(request, pk):
    about = get_object_or_404(About, id=pk)
    if request.method == 'POST':
        about.delete()
        return redirect('about_list')
    return render(request, 'admin/about_delete.html', {'about': about})


def service_header_create(request):
    if request.method == 'POST':
        form = ServiceHeaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_header_list')
    else:
        form = ServiceHeaderForm()
    return render(request, 'admin/service_header_create.html', {'form': form})


def service_header_list(request):
    service_headers = ServiceHeader.objects.all()
    return render(request, 'admin/service_header_list.html', {'service_headers': service_headers})


def service_header_update(request, pk):
    service_header = get_object_or_404(ServiceHeader, id=pk)
    if request.method == 'POST':
        form = ServiceHeaderForm(request.POST, instance=service_header)
        if form.is_valid():
            form.save()
            return redirect('service_header_list')
    else:
        form = ServiceHeaderForm(instance=service_header)
    return render(request, 'admin/service_header_update.html', {'form': form, 'service_header': service_header})


def service_header_delete(request, pk):
    service_header = get_object_or_404(ServiceHeader, id=pk)
    if request.method == 'POST':
        service_header.delete()
        return redirect('service_header_list')
    return render(request, 'admin/service_header_delete.html', {'service_header': service_header})


@login_required(login_url='/admin/')
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'admin/service_create.html', {'form': form})


@login_required(login_url='/admin/')
def service_list(request):
    services = Service.objects.all()
    return render(request, 'admin/service_list.html', {'services': services})


@login_required(login_url='/admin/')
def service_update(request, pk):
    service = get_object_or_404(Service, id=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'admin/service_update.html', {'form': form, 'service': service})


@login_required(login_url='/admin/')
def service_delete(request, pk):
    service = get_object_or_404(Service, id=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'admin/service_delete.html', {'service': service})


@login_required(login_url='/admin/')
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'admin/client_create.html', {'form': form})


@login_required(login_url='/admin/')
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'admin/client_list.html', {'clients': clients})


@login_required(login_url='/admin/')
def client_update(request, pk):
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'admin/client_update.html', {'form': form, 'client': client})


@login_required(login_url='/admin/')
def client_delete(request, pk):
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'admin/client_delete.html', {'client': client})


@login_required(login_url='/admin/')
def touch_create(request):
    if request.method == 'POST':
        form = TouchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('touch_list')
    else:
        form = TouchForm()

    return render(request, 'admin/touch_create.html', {'form': form})


@login_required(login_url='/admin/')
def touch_list(request):
    touches = Touch.objects.all()
    return render(request, 'admin/touch_list.html', {'touches': touches})


@login_required(login_url='/admin/')
def touch_update(request, pk):
    touch = get_object_or_404(Touch, id=pk)
    if request.method == 'POST':
        form = TouchForm(request.POST, request.FILES, instance=touch)
        if form.is_valid():
            form.save()
            return redirect('touch_list')
    else:
        form = TouchForm(instance=touch)

    return render(request, 'admin/touch_update.html', {'form': form, 'touch': touch})


@login_required(login_url='/admin/')
def touch_delete(request, pk):
    touch = get_object_or_404(Touch, id=pk)
    if request.method == 'POST':
        touch.delete()
        return redirect('touch_list')
    return render(request, 'admin/touch_delete.html', {'touch': touch})


@login_required(login_url='/admin/')
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'admin/team_create.html', {'form': form})


@login_required(login_url='/admin/')
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'admin/team_list.html', {'teams': teams})


@login_required(login_url='/admin/')
def team_update(request, pk):
    team = get_object_or_404(Team, id=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'admin/team_update.html', {'form': form, 'team': team})


@login_required(login_url='/admin/')
def team_delete(request, pk):
    team = get_object_or_404(Team, id=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'admin/team_delete.html', {'team': team})


@login_required(login_url='/admin/')
def guard_create(request):
    if request.method == 'POST':
        form = GuardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guard_list')
    else:
        form = GuardForm()
    return render(request, 'admin/guard_create.html', {'form': form})


@login_required(login_url='/admin/')
def guard_list(request):
    guards = Guard.objects.all()
    return render(request, 'admin/guard_list.html', {'guards': guards})


@login_required(login_url='/admin/')
def guard_update(request, pk):
    guard = get_object_or_404(Guard, id=pk)
    if request.method == 'POST':
        form = GuardForm(request.POST, request.FILES, instance=guard)
        if form.is_valid():
            form.save()
            return redirect('guard_list')
    else:
        form = GuardForm(instance=guard)
    return render(request, 'admin/guard_update.html', {'form': form, 'guard': guard})


@login_required(login_url='/admin/')
def guard_delete(request, pk):
    guard = get_object_or_404(Guard, id=pk)
    if request.method == 'POST':
        guard.delete()
        return redirect('guard_list')
    return render(request, 'admin/guard_delete.html', {'guard': guard})


@login_required(login_url='/admin/')
def info_create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_list')
    else:
        form = InfoForm()
    return render(request, 'admin/info_create.html', {'form': form})


@login_required(login_url='/admin/')
def info_list(request):
    infos = Info.objects.all()
    return render(request, 'admin/info_list.html', {'infos': infos})


@login_required(login_url='/admin/')
def info_update(request, pk):
    info = get_object_or_404(Info, id=pk)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('info_list')
    else:
        form = InfoForm(instance=info)
    return render(request, 'admin/info_update.html', {'form': form, 'info': info})


@login_required(login_url='/admin/')
def info_delete(request, pk):
    info = get_object_or_404(Info, id=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('info_list')
    return render(request, 'admin/info_delete.html', {'info': info})


@login_required(login_url='/admin/')
def contactus_create(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus_list')
    else:
        form = ContactUsForm()
    return render(request, 'admin/contact_us_create.html', {'form': form})


@login_required(login_url='/admin/')
def contactus_list(request):
    contactus_entries = ContactUs.objects.all()
    return render(request, 'admin/contact_us_list.html', {'contactus_entries': contactus_entries})


@login_required(login_url='/admin/')
def contactus_update(request, pk):
    contactus_entry = get_object_or_404(ContactUs, id=pk)
    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=contactus_entry)
        if form.is_valid():
            form.save()
            return redirect('contactus_list')
    else:
        form = ContactUsForm(instance=contactus_entry)
    return render(request, 'admin/contact_us_update.html', {'form': form, 'contactus_entry': contactus_entry})


@login_required(login_url='/admin/')
def contactus_delete(request, pk):
    contactus_entry = get_object_or_404(ContactUs, id=pk)
    if request.method == 'POST':
        contactus_entry.delete()
        return redirect('contactus_list')
    return render(request, 'admin/contact_us_delete.html', {'contactus_entry': contactus_entry})


@login_required(login_url='/admin/')
def subscribe_create(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscribe_list')
    else:
        form = SubscribeForm()
    return render(request, 'admin/subscribe_create.html', {'form': form})


@login_required(login_url='/admin/')
def subscribe_list(request):
    subscribes = Subscribe.objects.all()
    return render(request, 'admin/subscribe_list.html', {'subscribes': subscribes})


@login_required(login_url='/admin/')
def subscribe_update(request, pk):
    subscribe = get_object_or_404(Subscribe, id=pk)
    if request.method == 'POST':
        form = SubscribeForm(request.POST, instance=subscribe)
        if form.is_valid():
            form.save()
            return redirect('subscribe_list')
    else:
        form = SubscribeForm(instance=subscribe)
    return render(request, 'admin/subscribe_update.html', {'form': form, 'subscribe': subscribe})


@login_required(login_url='/admin/')
def subscribe_delete(request, pk):
    subscribe = get_object_or_404(Subscribe, id=pk)
    if request.method == 'POST':
        subscribe.delete()
        return redirect('subscribe_list')
    return render(request, 'admin/subscribe_delete.html', {'subscribe': subscribe})


@login_required(login_url='/admin/')
def footer_create(request):
    if request.method == "POST":
        form = FooterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('footer_list')
    else:
        form = FooterForm()
    return render(request, 'admin/footer_create.html', {'form': form})


@login_required(login_url='/admin/')
def footer_list(request):
    footers = Footer.objects.all()
    return render(request, 'admin/footer_list.html', {'footers': footers})


@login_required(login_url='/admin/')
def footer_update(request, pk):
    footer = get_object_or_404(Footer, id=pk)

    if request.method == "POST":
        form = FooterForm(request.POST, instance=footer)
        if form.is_valid():
            form.save()
            return redirect('footer_list')
    else:
        form = FooterForm(instance=footer)

    return render(request, 'admin/footer_update.html', {'form': form, 'footer': footer})


@login_required(login_url='/admin/')
def footer_delete(request, pk):
    footer = get_object_or_404(Footer, id=pk)

    if request.method == 'POST':
        footer.delete()
        return redirect('footer_list')

    return render(request, 'admin/footer_delete.html', {'footer': footer})


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


@login_required(login_url='/admin/')
def user_contact_create(request):
    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_contact_list')
    else:
        form = UserContactForm()
    return render(request, 'admin/user_contact_create.html', {'form': form})


@login_required(login_url='/admin/')
def user_contact_list(request):
    user_contacts = UserContact.objects.all()
    return render(request, 'admin/user_contact_list.html', {'user_contacts': user_contacts})


@login_required(login_url='/admin/')
def user_contact_update(request, pk):
    user_contact = get_object_or_404(UserContact, id=pk)
    if request.method == 'POST':
        form = UserContactForm(request.POST, instance=user_contact)
        if form.is_valid():
            form.save()
            return redirect('user_contact_list')
    else:
        form = UserContactForm(instance=user_contact)
    return render(request, 'admin/user_contact_update.html', {'form': form, 'user_contact': user_contact})


@login_required(login_url='/admin/')
def user_contact_delete(request, pk):
    user_contact = get_object_or_404(UserContact, id=pk)
    if request.method == 'POST':
        user_contact.delete()
        return redirect('user_contact_list')
    return render(request, 'admin/user_contact_delete.html', {'user_contact': user_contact})


# API

class UserContactListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить список всех контактов",
        responses={200: UserContactSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        contacts = UserContact.objects.all()
        serializer = UserContactSerializer(contacts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый контакт",
        request_body=UserContactSerializer,
        responses={201: UserContactSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = UserContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserContactDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить контакт",
        request_body=UserContactSerializer,
        responses={200: UserContactSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            contact = UserContact.objects.get(id=kwargs['pk'])
        except UserContact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частично обновить контакт",
        request_body=UserContactSerializer,
        responses={200: UserContactSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            contact = UserContact.objects.get(id=kwargs['pk'])
        except UserContact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить контакт",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            contact = UserContact.objects.get(id=kwargs['pk'])
        except UserContact.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import HeaderSerializer


class HeaderListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить список всех Header",
        responses={200: HeaderSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        headers = Header.objects.all()
        serializer = HeaderSerializer(headers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый Header",
        request_body=HeaderSerializer,
        responses={201: HeaderSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = HeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeaderDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить Header",
        request_body=HeaderSerializer,
        responses={200: HeaderSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            header = Header.objects.get(id=kwargs['pk'])
        except Header.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HeaderSerializer(header, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частично обновить Header",
        request_body=HeaderSerializer,
        responses={200: HeaderSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            header = Header.objects.get(id=kwargs['pk'])
        except Header.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HeaderSerializer(header, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить Header",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            header = Header.objects.get(id=kwargs['pk'])
        except Header.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        header.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import MenuSerializer


class MenuListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить список всех меню",
        responses={200: MenuSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый пункт меню",
        request_body=MenuSerializer,
        responses={201: MenuSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить пункт меню",
        request_body=MenuSerializer,
        responses={200: MenuSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            menu = Menu.objects.get(id=kwargs['pk'])
        except Menu.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частично обновить пункт меню",
        request_body=MenuSerializer,
        responses={200: MenuSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            menu = Menu.objects.get(id=kwargs['pk'])
        except Menu.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = MenuSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить пункт меню",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            menu = Menu.objects.get(id=kwargs['pk'])
        except Menu.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import SliderSerializer


class SliderListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all sliders",
        responses={200: SliderSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new slider",
        request_body=SliderSerializer,
        responses={201: SliderSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = SliderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SliderDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a slider",
        request_body=SliderSerializer,
        responses={200: SliderSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            slider = Slider.objects.get(id=kwargs['pk'])
        except Slider.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SliderSerializer(slider, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a slider",
        request_body=SliderSerializer,
        responses={200: SliderSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            slider = Slider.objects.get(id=kwargs['pk'])
        except Slider.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SliderSerializer(slider, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a slider",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            slider = Slider.objects.get(id=kwargs['pk'])
        except Slider.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        slider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import AboutSerializer


class AboutListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all About entries",
        responses={200: AboutSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        abouts = About.objects.all()
        serializer = AboutSerializer(abouts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new About entry",
        request_body=AboutSerializer,
        responses={201: AboutSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update an About entry",
        request_body=AboutSerializer,
        responses={200: AboutSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            about = About.objects.get(id=kwargs['pk'])
        except About.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an About entry",
        request_body=AboutSerializer,
        responses={200: AboutSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            about = About.objects.get(id=kwargs['pk'])
        except About.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an About entry",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            about = About.objects.get(id=kwargs['pk'])
        except About.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        about.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import ServiceHeaderSerializer


class ServiceHeaderListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Service Headers",
        responses={200: ServiceHeaderSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        headers = ServiceHeader.objects.all()
        serializer = ServiceHeaderSerializer(headers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Service Header",
        request_body=ServiceHeaderSerializer,
        responses={201: ServiceHeaderSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = ServiceHeaderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceHeaderDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Service Header",
        request_body=ServiceHeaderSerializer,
        responses={200: ServiceHeaderSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            header = ServiceHeader.objects.get(id=kwargs['pk'])
        except ServiceHeader.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceHeaderSerializer(header, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Service Header",
        request_body=ServiceHeaderSerializer,
        responses={200: ServiceHeaderSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            header = ServiceHeader.objects.get(id=kwargs['pk'])
        except ServiceHeader.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceHeaderSerializer(header, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Service Header",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            header = ServiceHeader.objects.get(id=kwargs['pk'])
        except ServiceHeader.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        header.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import ServiceSerializer


class ServiceListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Services",
        responses={200: ServiceSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Service",
        request_body=ServiceSerializer,
        responses={201: ServiceSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Service",
        request_body=ServiceSerializer,
        responses={200: ServiceSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            service = Service.objects.get(id=kwargs['pk'])
        except Service.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Service",
        request_body=ServiceSerializer,
        responses={200: ServiceSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            service = Service.objects.get(id=kwargs['pk'])
        except Service.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Service",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            service = Service.objects.get(id=kwargs['pk'])
        except Service.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import ClientSerializer


class ClientListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Clients",
        responses={200: ClientSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Client",
        request_body=ClientSerializer,
        responses={201: ClientSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Client",
        request_body=ClientSerializer,
        responses={200: ClientSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(id=kwargs['pk'])
        except Client.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Client",
        request_body=ClientSerializer,
        responses={200: ClientSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(id=kwargs['pk'])
        except Client.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Client",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            client = Client.objects.get(id=kwargs['pk'])
        except Client.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import TouchSerializer


class TouchListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Touch items",
        responses={200: TouchSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        touches = Touch.objects.all()
        serializer = TouchSerializer(touches, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Touch item",
        request_body=TouchSerializer,
        responses={201: TouchSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = TouchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TouchDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Touch item",
        request_body=TouchSerializer,
        responses={200: TouchSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            touch = Touch.objects.get(id=kwargs['pk'])
        except Touch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TouchSerializer(touch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Touch item",
        request_body=TouchSerializer,
        responses={200: TouchSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            touch = Touch.objects.get(id=kwargs['pk'])
        except Touch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TouchSerializer(touch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Touch item",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            touch = Touch.objects.get(id=kwargs['pk'])
        except Touch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        touch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import TeamSerializer


class TeamListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Team members",
        responses={200: TeamSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Team member",
        request_body=TeamSerializer,
        responses={201: TeamSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Team member",
        request_body=TeamSerializer,
        responses={200: TeamSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            team = Team.objects.get(id=kwargs['pk'])
        except Team.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Team member",
        request_body=TeamSerializer,
        responses={200: TeamSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            team = Team.objects.get(id=kwargs['pk'])
        except Team.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamSerializer(team, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Team member",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            team = Team.objects.get(id=kwargs['pk'])
        except Team.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import GuardSerializer


class GuardListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all guards",
        responses={200: GuardSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        guards = Guard.objects.all()
        serializer = GuardSerializer(guards, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new guard",
        request_body=GuardSerializer,
        responses={201: GuardSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = GuardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GuardDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a guard",
        request_body=GuardSerializer,
        responses={200: GuardSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            guard = Guard.objects.get(id=kwargs['pk'])
        except Guard.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = GuardSerializer(guard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a guard",
        request_body=GuardSerializer,
        responses={200: GuardSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            guard = Guard.objects.get(id=kwargs['pk'])
        except Guard.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = GuardSerializer(guard, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a guard",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            guard = Guard.objects.get(id=kwargs['pk'])
        except Guard.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        guard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import InfoSerializer


class InfoListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all info records",
        responses={200: InfoSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        info_list = Info.objects.all()
        serializer = InfoSerializer(info_list, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new info record",
        request_body=InfoSerializer,
        responses={201: InfoSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfoDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update an info record",
        request_body=InfoSerializer,
        responses={200: InfoSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            info = Info.objects.get(id=kwargs['pk'])
        except Info.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = InfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update an info record",
        request_body=InfoSerializer,
        responses={200: InfoSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            info = Info.objects.get(id=kwargs['pk'])
        except Info.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = InfoSerializer(info, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete an info record",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            info = Info.objects.get(id=kwargs['pk'])
        except Info.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import ContactUsSerializer


class ContactUsListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all ContactUs records",
        responses={200: ContactUsSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        contacts = ContactUs.objects.all()
        serializer = ContactUsSerializer(contacts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new ContactUs record",
        request_body=ContactUsSerializer,
        responses={201: ContactUsSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactUsDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a ContactUs record",
        request_body=ContactUsSerializer,
        responses={200: ContactUsSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            contact = ContactUs.objects.get(id=kwargs['pk'])
        except ContactUs.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactUsSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a ContactUs record",
        request_body=ContactUsSerializer,
        responses={200: ContactUsSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            contact = ContactUs.objects.get(id=kwargs['pk'])
        except ContactUs.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ContactUsSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a ContactUs record",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            contact = ContactUs.objects.get(id=kwargs['pk'])
        except ContactUs.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import SubscribeSerializer


class SubscribeListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Subscribe records",
        responses={200: SubscribeSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        subscriptions = Subscribe.objects.all()
        serializer = SubscribeSerializer(subscriptions, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Subscribe record",
        request_body=SubscribeSerializer,
        responses={201: SubscribeSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscribeDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Subscribe record",
        request_body=SubscribeSerializer,
        responses={200: SubscribeSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            subscription = Subscribe.objects.get(id=kwargs['pk'])
        except Subscribe.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubscribeSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Subscribe record",
        request_body=SubscribeSerializer,
        responses={200: SubscribeSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            subscription = Subscribe.objects.get(id=kwargs['pk'])
        except Subscribe.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubscribeSerializer(subscription, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Subscribe record",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            subscription = Subscribe.objects.get(id=kwargs['pk'])
        except Subscribe.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import FooterSerializer


class FooterListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve a list of all Footer records",
        responses={200: FooterSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        footers = Footer.objects.all()
        serializer = FooterSerializer(footers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Create a new Footer record",
        request_body=FooterSerializer,
        responses={201: FooterSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = FooterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FooterDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Update a Footer record",
        request_body=FooterSerializer,
        responses={200: FooterSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            footer = Footer.objects.get(id=kwargs['pk'])
        except Footer.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FooterSerializer(footer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Partially update a Footer record",
        request_body=FooterSerializer,
        responses={200: FooterSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            footer = Footer.objects.get(id=kwargs['pk'])
        except Footer.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = FooterSerializer(footer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Delete a Footer record",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            footer = Footer.objects.get(id=kwargs['pk'])
        except Footer.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        footer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from .serializers import HeaderTouchSerializer


class HeaderTouchListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Получить список всех HeaderTouch",
        responses={200: HeaderTouchSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        touches = HeaderTouch.objects.all()
        serializer = HeaderTouchSerializer(touches, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новый HeaderTouch",
        request_body=HeaderTouchSerializer,
        responses={201: HeaderTouchSerializer()},
    )
    def post(self, request, *args, **kwargs):
        serializer = HeaderTouchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HeaderTouchDetailAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Обновить HeaderTouch",
        request_body=HeaderTouchSerializer,
        responses={200: HeaderTouchSerializer()},
    )
    def put(self, request, *args, **kwargs):
        try:
            touch = HeaderTouch.objects.get(id=kwargs['pk'])
        except HeaderTouch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HeaderTouchSerializer(touch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Частично обновить HeaderTouch",
        request_body=HeaderTouchSerializer,
        responses={200: HeaderTouchSerializer()},
    )
    def patch(self, request, *args, **kwargs):
        try:
            touch = HeaderTouch.objects.get(id=kwargs['pk'])
        except HeaderTouch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = HeaderTouchSerializer(touch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить HeaderTouch",
        responses={204: "No Content"},
    )
    def delete(self, request, *args, **kwargs):
        try:
            touch = HeaderTouch.objects.get(id=kwargs['pk'])
        except HeaderTouch.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        touch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
