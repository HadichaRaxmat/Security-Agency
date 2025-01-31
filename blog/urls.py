from django.urls import path
from .views import home_view, service_view, guard_view, contact_view, about_view

urlpatterns = [
    path('', home_view, name="home"),
    path('service/', service_view),
    path('guard/', guard_view),
    path('contact/', contact_view),
    path('about/', about_view)
]