from django.urls import path
from .views import *

urlpatterns = [

    # ---------- TEMPLATE PAGES ----------

    path(
        "",
        home
    ),

    path(
        "user",
        user_page
    ),

    path(
        "admin-page",
        admin_page
    ),

    path(
        "user-signup-page",
        user_signup_page
    ),

    path(
        "user-login-page",
        user_login_page
    ),

    path(
        "user-main-page",
        user_main_page
    ),

    path(
        "create-task-page",
        create_task_page
    ),

    path(
        "view-task-page",
        view_task_page
    ),

    path(
        "update-task-page",
        update_task_page
    ),

    path(
        "delete-task-page",
        delete_task_page
    ),

    path(
        "admin-signup-page",
        admin_signup_page
    ),

    path(
        "admin-login-page",
        admin_login_page
    ),

    path(
        "admin-main-page",
        admin_main_page
    ),

    path(
        "admin-all-users-page",
        admin_all_users_page
    ),

    path(
        "admin-all-tasks-page",
        admin_all_tasks_page
    ),

    path(
        "admin-delete-tasks-page",
        admin_delete_tasks_page
    ),


    # ---------- USER APIs ----------

    path(
        "signup",
        user_signup
    ),

    path(
        "login",
        user_login
    ),

    path(
        "create-task",
        create_task
    ),

    path(
        "view-task",
        view_task
    ),

    path(
        "delete-task",
        delete_task
    ),

    path(
        "update-task",
        update_task
    ),


    # ---------- ADMIN APIs ----------

    path(
        "admin-signup",
        admin_signup
    ),

    path(
        "admin-login",
        admin_login
    ),

    path(
        "all-users",
        all_users
    ),

    path(
        "all-tasks",
        all_tasks
    ),

    path(
        "delete-task-admin",
        delete_task_admin
    ),

]