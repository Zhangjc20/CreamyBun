"""CreamyBun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from CreamyBunApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('log_up/',views.log_up), 
    path('log_in/',views.log_in),
    path('send_email/',views.send_email),
    path('log_off/',views.log_off),
    path('update_mobile/',views.update_mobile),
    path('get_material_zip/',views.get_material_zip),
]
