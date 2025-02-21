from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import views
from .views import (home_view, service_view, guard_view, contact_view, about_view,
                    admin_list, admin_create, admin_update, admin_delete, admin_logout)


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

    path('dashboard/', views.admin_view, name='dashboard'),
    path('admin/profile/', views.admin_profile, name='admin_profile'),
    path('admin/list/', admin_list, name='admin_list'),
    path('admin/create/', admin_create, name='admin_create'),
    path('admin/update/<int:user_id>/', admin_update, name='admin_update'),
    path('admin/delete/<int:user_id>/', admin_delete, name='admin_delete'),
    path('admin/logout/', admin_logout, name='admin_logout'),
    #user
    path('users/', views.users_list, name='users'),
    path('user/update/<int:pk>/', views.user_update, name='user_update'),
    path('user/delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Header
    path('header/list', views.HeaderListView.as_view(), name='header_list'),
    path('header/create/', views.HeaderCreateView.as_view(), name='header_create'),
    path('header/update/<int:pk>/', views.HeaderUpdateView.as_view(), name='header_update'),
    path('header/delete/<int:pk>/', views.HeaderDeleteView.as_view(), name='header_delete'),
    #menu
    path('menu/add/', views.MenuAddView.as_view(), name='menu_add'), #create
    path('menu/list/', views.MenuListView.as_view(), name='menu_list'), # Header list
    path('menu/update/<int:pk>/', views.MenuUpdateView.as_view(), name='menu_update'), #update
    path('menu/delete/<int:pk>/', views.MenuDeleteView.as_view(), name='menu_delete'), #delete
    path('menu/visibility/<int:pk>/', views.menu_toggle_visibility, name='menu_toggle_visibility'),
    # slider
    path('slider/create/', views.SliderCreateView.as_view(), name='slider_create'),
    path('slider/list/', views.SliderListView.as_view(), name='slider_list'),
    path('slider/update/<int:pk>/', views.SliderUpdateView.as_view(), name='slider_update'),
    path('slider/delete/<int:pk>/', views.SliderDeleteView.as_view(), name='slider_delete'),
    # about
    path('about/create/', views.AboutCreateView.as_view(), name='about_create'),
    path('about/list/', views.AboutListView.as_view(), name='about_list'),
    path('about/update/<int:pk>/', views.AboutUpdateView.as_view(), name='about_update'),
    path('about/delete/<int:pk>/', views.AboutDeleteView.as_view(), name='about_delete'),

    path('service-header/create/', views.ServiceHeaderCreateView.as_view(), name='service_header_create'),
    path('service-header/list/', views. ServiceHeaderListView.as_view, name='service_header_list'),
    path('service-header/update/<int:pk>/', views.ServiceHeaderUpdateView.as_view(), name='service_header_update'),
    path('service-header/delete/<int:pk>/', views.ServiceHeaderDeleteView.as_view(), name='service_header_delete'),

    path('service/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('service/list/', views.ServiceListView.as_view(), name='service_list'),
    path('service/update/<int:pk>/', views.ServiceUpdateView.as_view(), name='service_update'),
    path('service/delete/<int:pk>/', views.ServiceDeleteView.as_view(), name='service_delete'),

    path('client/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('client/list/', views.ClientListView.as_view(), name='client_list'),
    path('client/update/<int:pk>/', views.ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', views.ClientDeleteView.as_view(), name='client_delete'),

    path('touch/create/', views.TouchCreateView.as_view(), name='touch_create'),
    path('touch/list/', views.TouchListView.as_view(), name='touch_list'),
    path('touch/update/<int:pk>/', views.TouchUpdateVIew.as_view(), name='touch_update'),
    path('touch/delete/<int:pk>/', views.TouchDeleteView.as_view(), name='touch_delete'),

    path('team/create/', views.TeamCreateView.as_view(), name='team_create'),
    path('team/list', views.TeamListView.as_view(), name='team_list'),
    path('team/update/<int:pk>/', views.TeamUpdateView.as_view(), name='team_update'),
    path('team/delete/<int:pk>/', views.TeamDeleteVIew.as_view(), name='team_delete'),

    path('guard/create/', views.GuardCreateView.as_view(), name='guard_create'),
    path('guard/list/', views.GuardListView.as_view(), name='guard_list'),
    path('guard/update/<int:pk>/', views.GuardUpdateView.as_view(), name='guard_update'),
    path('guard/delete/<int:pk>/', views.GuardDeleteView.as_view(), name='guard_delete'),

    path('info/create/', views.InfoCreateView.as_view(), name='info_create'),
    path('info/list/', views.InfoListView.as_view(), name='info_list'),
    path('info/update/<int:pk>/', views.InfoUpdateView.as_view(), name='info_update'),
    path('info/delete/<int:pk>/', views.InfoDeleteView.as_view(), name='info_delete'),

    path('contact-us/create/', views.ContactusCreateView.as_view(), name='contactus_create'),
    path('contact-us/list/', views.ContactusListView.as_view(), name='contactus_list'),
    path('contact-us/update/<int:pk>/', views.ContactusUpdateView.as_view(), name='contactus_update'),
    path('contact-us/delete/<int:pk>/', views.ContactusDeleteView.as_view(), name='contactus_delete'),

    path('subscribe/create/', views.SubscribeCreateView.as_view(), name='subscribe_create'),
    path('subscribe/list/', views.SubscribeListView.as_view(), name='subscribe_list'),
    path('subscribe/update/<int:pk>/', views.SubscribeUpdateView.as_view(), name='subscribe_update'),
    path('subscribe/delete/<int:pk>/', views.SubscribeDeleteView.as_view(), name='subscribe_delete'),

    path('footer/create/', views.FooterCreateView.as_view(), name='footer_create'),
    path('footer/list/', views.FooterListView.as_view(), name='footer_list'),
    path('footer/update/<int:pk>/', views.FooterUpdateView.as_view, name='footer_update'),
    path('footer/delete/<int:pk>/', views.FooterDeleteView.as_view(), name='footer_delete'),
    path('footer/bulk-delete/', views.footer_bulk_delete, name='footer_bulk_delete'),

    path('user-contact/create/', views.UserContactCreateView.as_view(), name='user_contact_create'),
    path('user-contact/list/', views.UserContactListView.as_view(), name='user_contact_list'),
    path('user-contact/update/<int:pk>/', views.UserContactUpdateView.as_view(), name='user_contact_update'),
    path('user-contact/delete/<int:pk>/', views.UserContactDeleteView.as_view(), name='user_contact_delete'),
    path('user-contact/<int:contact_id>/read/', views.mark_as_read, name='mark_as_read'),




    # API

    re_path(r'^swagger(?P<format>\.json|\.yml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/user/contact/', views.UserContactListAPIView.as_view(), name='user-contact-list'),
    path('api/user/contact/<int:pk>/', views.UserContactDetailAPIView.as_view(), name='user-contact-detail'),
    path('api/header/', views.HeaderListAPIView.as_view(), name='header-list'),
    path('api/header/<int:pk>/', views.HeaderDetailAPIView.as_view(), name='header-detail'),
    path('api/menu/', views.MenuListAPIView.as_view(), name='menu-list'),
    path('api/menu/<int:pk>/', views.MenuDetailAPIView.as_view(), name='menu-detail'),
    path('api/header-touch/', views.HeaderTouchListAPIView.as_view(), name='header-touch-list'),
    path('api/header-touch/<int:pk>/', views.HeaderTouchDetailAPIView.as_view(), name='header-touch-detail'),
    path('api/slider/', views.SliderListAPIView.as_view(), name='slider-list'),
    path('api/slider/<int:pk>/', views.SliderDetailAPIView.as_view(), name='slider-detail'),
    path('api/about/', views.AboutListAPIView.as_view(), name='about-list'),
    path('api/about/<int:pk>/', views.AboutDetailAPIView.as_view(), name='about-detail'),
    path('api/service-header/', views.ServiceHeaderListAPIView.as_view(), name='service-header-list'),
    path('api/service-header/<int:pk>/', views.ServiceHeaderDetailAPIView.as_view(), name='service-header-detail'),
    path('api/service/', views.ServiceListAPIView.as_view(), name='service-list'),
    path('api/service/<int:pk>/', views.ServiceDetailAPIView.as_view(), name='service-detail'),
    path('api/client/', views.ClientListAPIView.as_view(), name='client-list'),
    path('api/client/<int:pk>/', views.ClientDetailAPIView.as_view(), name='client-detail'),
    path('api/touch/', views.TouchListAPIView.as_view(), name='touch-list'),
    path('api/touch/<int:pk>/', views.TouchDetailAPIView.as_view(), name='touch-detail'),
    path('api/team/', views.TeamListAPIView.as_view(), name='team-list'),
    path('api/team/<int:pk>/', views.TeamDetailAPIView.as_view(), name='team-detail'),
    path('api/guard/', views.GuardListAPIView.as_view(), name='guard-list'),
    path('api/guard/<int:pk>/', views.GuardDetailAPIView.as_view(), name='guard-detail'),
    path('api/info/', views.InfoListAPIView.as_view(), name='info-list'),
    path('api/info/<int:pk>/', views.InfoDetailAPIView.as_view(), name='info-detail'),
    path('api/contact/us/', views.ContactUsListAPIView.as_view(), name='contact-us-list'),
    path('api/contact/us/<int:pk>/', views.ContactUsDetailAPIView.as_view(), name='contact-us-detail'),
    path('api/subscribe/', views.SubscribeListAPIView.as_view(), name='subscribe-list'),
    path('api/subscribe/<int:pk>/', views.SubscribeDetailAPIView.as_view(), name='subscribe-detail'),
    path('api/footer/', views.FooterListAPIView.as_view(), name='footer-list'),
    path('api/footer/<int:pk>/', views.FooterDetailAPIView.as_view(), name='footer-detail'),
]