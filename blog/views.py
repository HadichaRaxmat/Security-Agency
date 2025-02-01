from django.shortcuts import render, redirect, get_object_or_404
from .models import Header, Menu, Slider
from .forms import HeaderForm, MenuForm, SliderForm


def home_view(request):
    header = Header.objects.all()
    d = {
        'header': header
    }
    return render(request, 'index.html', context=d)

def about_view(request):
    return render(request, 'about.html')

def service_view(request):
    return render(request, 'service.html')

def guard_view(request):
    return render(request, 'guard.html')

def contact_view(request):
    return render(request, 'contact.html')

def admin_view(request):
    return render(request, 'admin/index.html')




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



def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
        return render(request, 'admin/menu_create.html', {'form': form})


def menu_list(request):
    menu = Menu.objects.all()
    return render(request, 'admin/menu_list.html', {'menu': menu})


def menu_update(request, pk):
    menu = get_object_or_404(Menu, id=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'admin/menu_update.html', {'form': form, 'menu': menu})


def menu_delete(request, pk):
    menu = get_object_or_404(Menu, id=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, 'admin/menu_delete.html', {'menu': menu})


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
