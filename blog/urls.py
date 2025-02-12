from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import views
from .views import (home_view, service_view, guard_view, contact_view, about_view, header_list, header_create,
                    header_delete, header_update, menu_update, menu_list, menu_add, slider_delete,
                    slider_update, slider_list, slider_create, about_list, about_create, about_update, about_delete,
                    admin_list, admin_create, admin_update, admin_delete, admin_logout, admin_view)


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Документация API для вашего проекта",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your.email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('', home_view, name="home"),
    path('service/', service_view),
    path('guard/', guard_view),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', admin_view, name='dashboard'),
    path('admin/profile/', views.admin_profile, name='admin_profile'),
    path("admin/profile/partial/", views.admin_profile_partial, name="admin_profile_partial"),
    path('admin/list/', admin_list, name='admin_list'),
    path('admin/create/', admin_create, name='admin_create'),
    path('admin/update/<int:user_id>/', admin_update, name='admin_update'),
    path('admin/delete/<int:user_id>/', admin_delete, name='admin_delete'),
    path('admin/logout/', admin_logout, name='admin_logout'),
    #user
    path('users/', views.users_list, name='users'),
    path('user/update/<int:pk>/', views.user_update, name='user_update'),
    path('user/delete/<int:pk>/', views.user_delete, name='user_delete'),
    # Header
    path('header/create/', header_create, name='header_create'), #create
    path('header/list/', header_list, name='header_list'), # Header list
    path('header/update/<int:pk>/', header_update, name='header_update'), #update
    path('header/delete/<int:pk>/', header_delete, name='header_delete'), #delete
    #menu
    path('menu/add/', menu_add, name='menu_add'), #create
    path('menu/list/', menu_list, name='menu_list'), # Header list
    path('menu/update/<int:pk>/', menu_update, name='menu_update'), #update
    path('menu/delete/<int:pk>/', views.menu_delete, name='menu_delete'), #delete
    path('menu/visibility/<int:pk>/', views.menu_toggle_visibility, name='menu_toggle_visibility'),
    # slider
    path('slider/create/', slider_create, name='slider_create'),
    path('slider/list/', slider_list, name='slider_list'),
    path('slider/update/<int:pk>/', slider_update, name='slider_update'),
    path('slider/delete/<int:pk>/', slider_delete, name='slider_delete'),
    # about
    path('about/create/', about_create, name='about_create'),
    path('about/list/', about_list, name='about_list'),
    path('about/update/<int:pk>/', about_update, name='about_update'),
    path('about/delete/<int:pk>/', about_delete, name='about_delete'),

    path('service-header/create/', views.service_header_create, name='service_header_create'),
    path('service-header/list/', views.service_header_list, name='service_header_list'),
    path('service-header/update/<int:pk>/', views.service_header_update, name='service_header_update'),
    path('service-header/delete/<int:pk>/', views.service_header_delete, name='service_header_delete'),

    path('service/create/', views.service_create, name='service_create'),
    path('service/list/', views.service_list, name='service_list'),
    path('service/update/<int:pk>/', views.service_update, name='service_update'),
    path('service/delete/<int:pk>/', views.service_delete, name='service_delete'),

    path('client/create/', views.client_create, name='client_create'),
    path('client/list/', views.client_list, name='client_list'),
    path('client/update/<int:pk>/', views.client_update, name='client_update'),
    path('client/delete/<int:pk>/', views.client_delete, name='client_delete'),

    path('touch/create/', views.touch_create, name='touch_create'),
    path('touch/list/', views.touch_list, name='touch_list'),
    path('touch/update/<int:pk>/', views.touch_update, name='touch_update'),
    path('touch/delete/<int:pk>/', views.touch_delete, name='touch_delete'),

    path('team/create/', views.team_create, name='team_create'),
    path('team/list', views.team_list, name='team_list'),
    path('team/update/<int:pk>/', views.team_update, name='team_update'),
    path('team/delete/<int:pk>/', views.team_delete, name='team_delete'),

    path('guard/create/', views.guard_create, name='guard_create'),
    path('guard/list/', views.guard_list, name='guard_list'),
    path('guard/update/<int:pk>/', views.guard_update, name='guard_update'),
    path('guard/delete/<int:pk>/', views.guard_delete, name='guard_delete'),

    path('info/create/', views.info_create, name='info_create'),
    path('info/list/', views.info_list, name='info_list'),
    path('info/update/<int:pk>/', views.info_update, name='info_update'),
    path('info/delete/<int:pk>/', views.info_delete, name='info_delete'),

    path('contact-us/create/', views.contactus_create, name='contactus_create'),
    path('contact-us/list/', views.contactus_list, name='contactus_list'),
    path('contact-us/update/<int:pk>/', views.contactus_update, name='contactus_update'),
    path('contact-us/delete/<int:pk>/', views.contactus_delete, name='contactus_delete'),

    path('subscribe/create/', views.subscribe_create, name='subscribe_create'),
    path('subscribe/list/', views.subscribe_list, name='subscribe_list'),
    path('subscribe/update/<int:pk>/', views.subscribe_update, name='subscribe_update'),
    path('subscribe/delete/<int:pk>/', views.subscribe_delete, name='subscribe_delete'),

    path('footer/create/', views.footer_create, name='footer_create'),
    path('footer/list/', views.footer_list, name='footer_list'),
    path('footer/update/<int:pk>/', views.footer_update, name='footer_update'),
    path('footer/delete/<int:pk>/', views.footer_delete, name='footer_delete'),
    path('footer/bulk-delete/', views.footer_bulk_delete, name='footer_bulk_delete'),

    path('user-contact/create/', views.user_contact_create, name='user_contact_create'),
    path('user-contact/list/', views.user_contact_list, name='user_contact_list'),
    path('user-contact/update/<int:pk>/', views.user_contact_update, name='user_contact_update'),
    path('user-contact/delete/<int:pk>/', views.user_contact_delete, name='user_contact_delete'),
]