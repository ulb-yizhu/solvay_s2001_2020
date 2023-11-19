"""
URL configuration for ukraine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from first_ukraine.views.login_view import login_view
from first_ukraine.views.register_view import register_view
from first_ukraine.views.welcome_view import welcome_view
from first_ukraine.views.new_establishment_view import register_establishment
from first_ukraine.views.reservation_view import register_reservation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_view),
    path('register', register_view),
    path('welcome', welcome_view),
    path('new_establishment', register_establishment),
    path('reservation/<int:establishment_id>', register_reservation)
]
