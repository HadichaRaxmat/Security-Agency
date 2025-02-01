from django.urls import path
from .views import (home_view, service_view, guard_view, contact_view, about_view, header_list, header_create,
                    header_delete, header_update, menu_delete, menu_update, menu_list, menu_create, slider_delete, slider_update, slider_list, slider_create)

urlpatterns = [
    path('', home_view, name="home"),
    path('service/', service_view),
    path('guard/', guard_view),
    path('contact/', contact_view),
    path('about/', about_view),
    # Header
    path('header/create/', header_create, name='header_create'), #create
    path('header/list/', header_list, name='header_list'), # Header list
    path('header/update/<int:pk>/', header_update, name='header_update'), #update
    path('header/delete/<int:pk>/', header_delete, name='header_delete'), #delete
    #menu
    path('menu/create/', menu_create, name='menu_create'), #create
    path('menu/list/', menu_list, name='menu_list'), # Header list
    path('menu/update/<int:pk>/', menu_update, name='menu_update'), #update
    path('menu/delete/<int:pk>/', menu_delete, name='menu_delete'), #delete
    # slider
    path('slider/create/', slider_create, name='slider_create'),
    path('slider/list/', slider_list, name='slider_list'),
    path('slider/update/<int:pk>/', slider_update, name='slider_update'),
    path('slider/delete/<int:pk>/', slider_delete, name='slider_delete'),
]