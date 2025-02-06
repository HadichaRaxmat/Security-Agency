from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .models import Header, Menu, Slider, About, ServiceHeader, Service, Client, Touch, Team, Guard, Info, ContactUs, \
    Subscribe, Footer, UserContact, CustomUser
from .forms import (HeaderForm, MenuForm, SliderForm, AboutForm, ServiceHeaderForm, ServiceForm, ClientForm, TouchForm, \
    TeamForm, GuardForm, InfoForm, ContactUsForm, SubscribeForm, FooterForm, UserContactForm, AdminUserCreationForm,
                    CustomUserCreationUserForm, AdminUserAuthenticationForm, CustomAuthenticationForm)


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
    d = {
        'header': header,
        'contactus': contactus,
        'menu': menu,
        'about': about,
        'info': info,
        'subscribe': subscribe,

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
    current_url = request.path
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
    if request.method == 'POST':
        data = request.POST
        contact = UserContact.objects.create(name=data['name'], email=data['email'], phone=data['phone'], message=data['message'])
        contact.save()
        return redirect('/')
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
        'current_url': current_url

    }
    return render(request, 'contact.html', context=d)



@login_required(login_url='/admin/')
def admin_view(request):
    return render(request, 'admin/index.html')

@login_required(login_url='/admin/')
def admin_list(request):
    users = CustomUser.objects.filter(is_staff=True)
    return render(request, 'admin/admin_list.html', {'users': users})

@login_required(login_url='/admin/')
def admin_create(request):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to create an admin.")
        return redirect('dashboard')

    if request.method == "POST":
        form = AdminUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_admin = True
            user.save()
            messages.success(request, f"Admin {user.email} created successfully.")
            return redirect('admin_list')

    else:
        form = AdminUserCreationForm()

    return render(request, 'admin/admin_create.html', {'form': form})


@login_required(login_url='/admin/')
def admin_update(request, user_id):
    CustomUser = get_user_model()
    user = get_object_or_404(CustomUser, id=user_id)

    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to edit admin users.")
        return redirect('admin_list')

    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin details updated successfully.")
            return redirect('admin_list')
    else:
        form = AdminUserCreationForm(instance=user)

    return render(request, 'admin/admin_update.html', {'form': form})


@login_required(login_url='/admin/')
def admin_delete(request, user_id):
    CustomUser = get_user_model()
    user = get_object_or_404(CustomUser, id=user_id)

    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to delete admin users.")
        return redirect('admin_list')

    if request.method == 'POST':
        user.delete()
        messages.success(request, "Admin user deleted successfully.")
        return redirect('admin_list')
    return render(request, 'admin/admin_delete.html', {'admin': user})


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


def login_view(request):
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


def logout_view(request):
    logout(request)
    return redirect('/')


def users_list(request):
    users = CustomUser.objects.all()
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
            url = menu_instance.get_url()
            return redirect("menu_list")
    else:
        form = MenuForm()

    return render(request, "admin/menu_add.html", {"form": form})


def menu_update(request, pk):
    menu = get_object_or_404(Menu, pk=pk)

    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)

        if form.is_valid():
            form.save()
            return redirect("menu_list")
    else:
        form = MenuForm(instance=menu)

    return render(request, "admin/menu_update.html", {"form": form})




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


def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'admin/service_create.html', {'form': form})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'admin/service_list.html', {'services': services})

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

def service_delete(request, pk):
    service = get_object_or_404(Service, id=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'admin/service_delete.html', {'service': service})


def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'admin/client_create.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'admin/client_list.html', {'clients': clients})

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

def client_delete(request, pk):
    client = get_object_or_404(Client, id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'admin/client_delete.html', {'client': client})


def touch_create(request):
    if request.method == 'POST':
        form = TouchForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('touch_list')
    else:
        form = TouchForm()

    return render(request, 'admin/touch_create.html', {'form': form})

def touch_list(request):
    touches = Touch.objects.all()
    return render(request, 'admin/touch_list.html', {'touches': touches})

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

def touch_delete(request, pk):
    touch = get_object_or_404(Touch, id=pk)
    if request.method == 'POST':
        touch.delete()
        return redirect('touch_list')
    return render(request, 'admin/touch_delete.html', {'touch': touch})


def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'admin/team_create.html', {'form': form})

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'admin/team_list.html', {'teams': teams})

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

def team_delete(request, pk):
    team = get_object_or_404(Team, id=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'admin/team_delete.html', {'team': team})


def guard_create(request):
    if request.method == 'POST':
        form = GuardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guard_list')
    else:
        form = GuardForm()
    return render(request, 'admin/guard_create.html', {'form': form})

def guard_list(request):
    guards = Guard.objects.all()
    return render(request, 'admin/guard_list.html', {'guards': guards})

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

def guard_delete(request, pk):
    guard = get_object_or_404(Guard, id=pk)
    if request.method == 'POST':
        guard.delete()
        return redirect('guard_list')
    return render(request, 'admin/guard_delete.html', {'guard': guard})


def info_create(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_list')
    else:
        form = InfoForm()
    return render(request, 'admin/info_create.html', {'form': form})

def info_list(request):
    infos = Info.objects.all()
    return render(request, 'admin/info_list.html', {'infos': infos})

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

def info_delete(request, pk):
    info = get_object_or_404(Info, id=pk)
    if request.method == 'POST':
        info.delete()
        return redirect('info_list')
    return render(request, 'admin/info_delete.html', {'info': info})



def contactus_create(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus_list')
    else:
        form = ContactUsForm()
    return render(request, 'admin/contact_us_create.html', {'form': form})

def contactus_list(request):
    contactus_entries = ContactUs.objects.all()
    return render(request, 'admin/contact_us_list.html', {'contactus_entries': contactus_entries})

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

def contactus_delete(request, pk):
    contactus_entry = get_object_or_404(ContactUs, id=pk)
    if request.method == 'POST':
        contactus_entry.delete()
        return redirect('contactus_list')
    return render(request, 'admin/contact_us_delete.html', {'contactus_entry': contactus_entry})


def subscribe_create(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscribe_list')
    else:
        form = SubscribeForm()
    return render(request, 'admin/subscribe_create.html', {'form': form})

def subscribe_list(request):
    subscribes = Subscribe.objects.all()
    return render(request, 'admin/subscribe_list.html', {'subscribes': subscribes})

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

def subscribe_delete(request, pk):
    subscribe = get_object_or_404(Subscribe, id=pk)
    if request.method == 'POST':
        subscribe.delete()
        return redirect('subscribe_list')
    return render(request, 'admin/subscribe_delete.html', {'subscribe': subscribe})


def footer_create(request):
    if request.method == 'POST':
        form = FooterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('footer_list')
    else:
        form = FooterForm()
    return render(request, 'admin/footer_create.html', {'form': form})

def footer_list(request):
    footers = Footer.objects.all()
    return render(request, 'admin/footer_list.html', {'footers': footers})

def footer_update(request, pk):
    footer = get_object_or_404(Footer, id=pk)
    if request.method == 'POST':
        form = FooterForm(request.POST, instance=footer)
        if form.is_valid():
            form.save()
            return redirect('footer_list')
    else:
        form = FooterForm(instance=footer)
    return render(request, 'admin/footer_update.html', {'form': form, 'footer': footer})

def footer_delete(request, pk):
    footer = get_object_or_404(Footer, id=pk)
    if request.method == 'POST':
        footer.delete()
        return redirect('footer_list')
    return render(request, 'admin/footer_delete.html', {'footer': footer})


def user_contact_create(request):
    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_contact_list')
    else:
        form = UserContactForm()
    return render(request, 'admin/user_contact_create.html', {'form': form})

def user_contact_list(request):
    user_contacts = UserContact.objects.all()
    return render(request, 'admin/user_contact_list.html', {'user_contacts': user_contacts})

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

def user_contact_delete(request, pk):
    user_contact = get_object_or_404(UserContact, id=pk)
    if request.method == 'POST':
        user_contact.delete()
        return redirect('user_contact_list')
    return render(request, 'admin/user_contact_delete.html', {'user_contact': user_contact})