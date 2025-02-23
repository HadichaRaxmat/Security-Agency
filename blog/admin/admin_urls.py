from django.urls import path
from blog.services import auth_service
from blog.admin import admin_views
app_name = 'admin'

urlpatterns = [
    path('dashboard/', admin_views.admin_view, name='dashboard'),
    path('profile/', admin_views.AdminProfileView.as_view(), name='admin_profile'),

    path('admin/list/', admin_views.AdminListView.as_view(), name='admin_list'),
    path('admin/create/', admin_views.AdminCreateView.as_view(), name='admin_create'),
    path('admin/update/<int:user_id>/', admin_views.AdminUpdateView.as_view(), name='admin_update'),
    path('admin/delete/<int:user_id>/', admin_views.AdminDeleteView.as_view(), name='admin_delete'),

    path('logout/', auth_service.admin_logout, name='admin_logout'),

    path('users/', admin_views.UsersListView.as_view(), name='user_list'),
    path('user/update/<int:pk>/', admin_views.UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', admin_views.UserDeleteView.as_view(), name='user_delete'),

# Header
    path('header/list', admin_views.HeaderListView.as_view(), name='header_list'),
    path('header/create/', admin_views.HeaderCreateView.as_view(), name='header_create'),
    path('header/update/<int:pk>/', admin_views.HeaderUpdateView.as_view(), name='header_update'),
    path('header/delete/<int:pk>/', admin_views.HeaderDeleteView.as_view(), name='header_delete'),
    #menu
    path('menu/add/', admin_views.MenuAddView.as_view(), name='menu_add'), #create
    path('menu/list/', admin_views.MenuListView.as_view(), name='menu_list'), # Header list
    path('menu/update/<int:pk>/', admin_views.MenuUpdateView.as_view(), name='menu_update'), #update
    path('menu/delete/<int:pk>/', admin_views.MenuDeleteView.as_view(), name='menu_delete'), #delete
    path('menu/visibility/<int:pk>/', admin_views.menu_toggle_visibility, name='menu_toggle_visibility'),
    # slider
    path('slider/create/', admin_views.SliderCreateView.as_view(), name='slider_create'),
    path('slider/list/', admin_views.SliderListView.as_view(), name='slider_list'),
    path('slider/update/<int:pk>/', admin_views.SliderUpdateView.as_view(), name='slider_update'),
    path('slider/delete/<int:pk>/', admin_views.SliderDeleteView.as_view(), name='slider_delete'),
    # about
    path('about/create/', admin_views.AboutCreateView.as_view(), name='about_create'),
    path('about/list/', admin_views.AboutListView.as_view(), name='about_list'),
    path('about/update/<int:pk>/', admin_views.AboutUpdateView.as_view(), name='about_update'),
    path('about/delete/<int:pk>/', admin_views.AboutDeleteView.as_view(), name='about_delete'),

    path('service-header/create/', admin_views.ServiceHeaderCreateView.as_view(), name='service_header_create'),
    path('service-header/list/', admin_views. ServiceHeaderListView.as_view(), name='service_header_list'),
    path('service-header/update/<int:pk>/', admin_views.ServiceHeaderUpdateView.as_view(), name='service_header_update'),
    path('service-header/delete/<int:pk>/', admin_views.ServiceHeaderDeleteView.as_view(), name='service_header_delete'),

    path('service/create/', admin_views.ServiceCreateView.as_view(), name='service_create'),
    path('service/list/', admin_views.ServiceListView.as_view(), name='service_list'),
    path('service/update/<int:pk>/', admin_views.ServiceUpdateView.as_view(), name='service_update'),
    path('service/delete/<int:pk>/', admin_views.ServiceDeleteView.as_view(), name='service_delete'),

    path('client/create/', admin_views.ClientCreateView.as_view(), name='client_create'),
    path('client/list/', admin_views.ClientListView.as_view(), name='client_list'),
    path('client/update/<int:pk>/', admin_views.ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', admin_views.ClientDeleteView.as_view(), name='client_delete'),

    path('touch/create/', admin_views.TouchCreateView.as_view(), name='touch_create'),
    path('touch/list/', admin_views.TouchListView.as_view(), name='touch_list'),
    path('touch/update/<int:pk>/', admin_views.TouchUpdateVIew.as_view(), name='touch_update'),
    path('touch/delete/<int:pk>/', admin_views.TouchDeleteView.as_view(), name='touch_delete'),

    path('team/create/', admin_views.TeamCreateView.as_view(), name='team_create'),
    path('team/list', admin_views.TeamListView.as_view(), name='team_list'),
    path('team/update/<int:pk>/', admin_views.TeamUpdateView.as_view(), name='team_update'),
    path('team/delete/<int:pk>/', admin_views.TeamDeleteVIew.as_view(), name='team_delete'),

    path('guard/create/', admin_views.GuardCreateView.as_view(), name='guard_create'),
    path('guard/list/', admin_views.GuardListView.as_view(), name='guard_list'),
    path('guard/update/<int:pk>/', admin_views.GuardUpdateView.as_view(), name='guard_update'),
    path('guard/delete/<int:pk>/', admin_views.GuardDeleteView.as_view(), name='guard_delete'),

    path('info/create/', admin_views.InfoCreateView.as_view(), name='info_create'),
    path('info/list/', admin_views.InfoListView.as_view(), name='info_list'),
    path('info/update/<int:pk>/', admin_views.InfoUpdateView.as_view(), name='info_update'),
    path('info/delete/<int:pk>/', admin_views.InfoDeleteView.as_view(), name='info_delete'),

    path('contact-us/create/', admin_views.ContactusCreateView.as_view(), name='contactus_create'),
    path('contact-us/list/', admin_views.ContactusListView.as_view(), name='contactus_list'),
    path('contact-us/update/<int:pk>/', admin_views.ContactusUpdateView.as_view(), name='contactus_update'),
    path('contact-us/delete/<int:pk>/', admin_views.ContactusDeleteView.as_view(), name='contactus_delete'),

    path('subscribe/create/', admin_views.SubscribeCreateView.as_view(), name='subscribe_create'),
    path('subscribe/list/', admin_views.SubscribeListView.as_view(), name='subscribe_list'),
    path('subscribe/update/<int:pk>/', admin_views.SubscribeUpdateView.as_view(), name='subscribe_update'),
    path('subscribe/delete/<int:pk>/', admin_views.SubscribeDeleteView.as_view(), name='subscribe_delete'),

    path('footer/create/', admin_views.FooterCreateView.as_view(), name='footer_create'),
    path('footer/list/', admin_views.FooterListView.as_view(), name='footer_list'),
    path('footer/update/<int:pk>/', admin_views.FooterUpdateView.as_view, name='footer_update'),
    path('footer/delete/<int:pk>/', admin_views.FooterDeleteView.as_view(), name='footer_delete'),
    path('footer/bulk-delete/', admin_views.footer_bulk_delete, name='footer_bulk_delete'),

    path('user-contact/create/', admin_views.UserContactCreateView.as_view(), name='user_contact_create'),
    path('user-contact/list/', admin_views.UserContactListView.as_view(), name='user_contact_list'),
    path('user-contact/update/<int:pk>/', admin_views.UserContactUpdateView.as_view(), name='user_contact_update'),
    path('user-contact/delete/<int:pk>/', admin_views.UserContactDeleteView.as_view(), name='user_contact_delete'),
    path('user-contact/<int:contact_id>/read/', admin_views.mark_as_read, name='mark_as_read'),
]