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
    path('log_up/', views.log_up),
    path('log_in/', views.log_in),
    path('send_email/', views.send_email),
    path('change_avatar/', views.change_avatar),
    path('update_username/', views.update_username),
    path('update_email/', views.update_email),
    path('log_off/', views.log_off),
    path('update_mobile/', views.update_mobile),
    path('get_material_zip/', views.get_material_zip),
    path('handle_release_action/', views.handle_release_action),
    path('release_task/', views.release_task),
    path('get_user_basic_info/', views.get_user_basic_info),
    path('get_task_basic_info/', views.get_task_basic_info),
    path('get_user_released_task_info/', views.get_user_released_task_info),
    path('get_user_received_task_info/', views.get_user_received_task_info),
    path('get_user_bonus_info/', views.get_user_bonus_info),
    path('get_user_activity_info/', views.get_user_activity_info),
    path('get_sorted_tasks/', views.get_sorted_tasks),
    path('clock_in/', views.clock_in),
    path('get_user_settings_info/', views.get_user_settings_info),
    path('reset_password/', views.reset_password),
    path('get_current_rate_info/', views.get_current_rate_info),
    path('change_current_rate_info/', views.change_current_rate_info),
    path('submit_feedback/', views.submit_feedback),
    path('perform_basic_info/', views.perform_basic_info),
    path('get_admin_username_and_password/', views.get_admin_username_and_password),
    path('set_admin_username_and_password/', views.set_admin_username_and_password),
    path('perform_problem_material/', views.perform_problem_material),
    path('uck_me/', views.uck_me),
    path('submit_feedback/', views.submit_feedback),
    path('final_submit/', views.final_submit),
    path('get_feedback/', views.get_feedback),
    path('stream_video/<path>/', views.stream_video),
    path('send_feedback_email/', views.send_feedback_email),
    path('handle_feedback_email/', views.handle_feedback_email),
    path('delete_feedback/', views.delete_feedback),
    path('add_reported_task/',views.add_reported_task),
    path('get_examining_tasks/',views.get_examining_tasks),
    path('delete_reported_task/',views.delete_reported_task),
    path('get_reported_task/',views.get_reported_task),
    path('send_report_email/',views.send_report_email),
    path('get_avatar/',views.get_avatar),
    path('receive_task/',views.receive_task),
    path('submit_answer/',views.submit_answer),
    path('get_release_info/',views.get_release_info),
    path('download_task_answer/',views.download_task_answer),
    path('top_up/',views.top_up),
    path('withdraw_money/',views.withdraw_money),
    path('update_phone/',views.update_phone)
]
