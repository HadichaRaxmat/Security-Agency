from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import views
from .views import (home_view, service_view, guard_view, contact_view, about_view,)
from blog.services import auth_service


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


    #user
    path('signup/', auth_service.AuthView.as_view(), name='signup'),
    path('signin/', auth_service.AuthView.as_view(), name='login'),
    path('logout/', auth_service.logout_view, name='logout'),





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