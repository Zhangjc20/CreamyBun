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
    path('change_avatar/',views.change_avatar),
    path('update_username/',views.update_username),
    path('update_email/',views.update_email),
    path('log_off/',views.log_off),
    path('update_mobile/',views.update_mobile),
    path('get_material_zip/',views.get_material_zip),
    path('handle_release_action/',views.handle_release_action),
    path('release_task/',views.release_task),
    path('get_user_basic_info/',views.get_user_basic_info),
    path('get_task_basic_info/',views.get_task_basic_info),
    path('get_user_released_task_info/',views.get_user_released_task_info),
    path('get_user_received_task_info/',views.get_user_received_task_info),
    path('get_user_bonus_info/',views.get_user_bonus_info),
    path('get_user_activity_info/',views.get_user_activity_info),
    path('clock_in/',views.clock_in),
    path('get_user_settings_info/',views.get_user_settings_info),
    path('reset_password/',views.reset_password),
    path('submit_feedback/',views.submit_feedback),
]
