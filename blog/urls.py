from django.urls import path
from .views import (home_view, service_view, guard_view, contact_view, about_view,)
from blog.services import auth_service


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
]