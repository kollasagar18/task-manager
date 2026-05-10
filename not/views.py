from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.hashers import (
    make_password,
    check_password
)

from .db import db_con


from django.shortcuts import render


def home(request):
    return render(
        request,
        "home.html"
    )


def user_page(request):
    return render(
        request,
        "user.html"
    )


def user_signup_page(request):
    return render(
        request,
        "user_signup.html"
    )


def user_login_page(request):
    return render(
        request,
        "user_login.html"
    )


def user_main_page(request):
    return render(
        request,
        "user_main.html"
    )


def create_task_page(request):
    return render(
        request,
        "create_task.html"
    )


def view_task_page(request):
    return render(
        request,
        "view_task.html"
    )


def update_task_page(request):
    return render(
        request,
        "update_task.html"
    )


def delete_task_page(request):
    return render(
        request,
        "delete_task.html"
    )


def admin_page(request):
    return render(
        request,
        "admin.html"
    )


def admin_signup_page(request):
    return render(
        request,
        "admin_signup.html"
    )


def admin_login_page(request):
    return render(
        request,
        "admin_login.html"
    )


def admin_main_page(request):
    return render(
        request,
        "admin_main.html"
    )


def admin_all_users_page(request):
    return render(
        request,
        "admin_all_users.html"
    )


def admin_all_tasks_page(request):
    return render(
        request,
        "admin_all_tasks.html"
    )


def admin_delete_tasks_page(request):
    return render(
        request,
        "admin_delete_tasks.html"
    )
def user_signup(request):

    if request.method == "POST":

        db = db_con()
        cu = db.cursor()

        name = request.POST.get(
            "name"
        )

        phone_num = request.POST.get(
            "phone_num"
        )

        password = request.POST.get(
            "password"
        )

        re_password = request.POST.get(
            "re_password"
        )

        if not name or not phone_num or not password:

            return render(
                request,
                "user_signup.html",
                {
                    "message":
                    "All fields are required"
                }
            )

        if password != re_password:

            return render(
                request,
                "user_signup.html",
                {
                    "message":
                    "Passwords do not match"
                }
            )

        hashed_password = make_password(
            password
        )

        cu.execute(
            """
            INSERT INTO users
            (name,password,phone_num,title,description)
            VALUES (%s,%s,%s,%s,%s)
            """,
            (
                name,
                hashed_password,
                phone_num,
                "NO TITLE",
                "NO DESCRIPTION"
            )
        )

        db.commit()

        db.close()

        return redirect(
            "/user-login-page"
        )

    return render(
        request,
        "user_signup.html"
    )

@api_view(["POST"])
def user_login(request):

    if request.method == "POST":

        db = db_con()
        cu = db.cursor()

        name = request.POST.get(
            "name"
        )

        phone_num = request.POST.get(
            "phone_num"
        )

        password = request.POST.get(
            "password"
        )

        cu.execute(
            """
            SELECT password
            FROM users
            WHERE name=%s
            AND phone_num=%s
            """,
            (
                name,
                phone_num
            )
        )

        user = cu.fetchone()

        if user:

            stored_password = user[0]

            if check_password(
                password,
                stored_password
            ):

                return redirect(
                    "/user-main-page"
                )

            else:

                return render(
                    request,
                    "user_login.html",
                    {
                        "message":
                        "Wrong Password"
                    }
                )

        return render(
            request,
            "user_login.html",
            {
                "message":
                "User Not Found"
            }
        )

    return render(
        request,
        "user_login.html"
    )



def create_task(request):

    if request.method == "POST":

        db = db_con()
        cu = db.cursor()

        name = request.POST.get(
            "name"
        )

        phone_num = request.POST.get(
            "phone_num"
        )

        title = request.POST.get(
            "title"
        )

        description = request.POST.get(
            "description"
        )

        cu.execute(
            """
            UPDATE users
            SET title=%s,
                description=%s
            WHERE name=%s
            AND phone_num=%s
            """,
            (
                title,
                description,
                name,
                phone_num
            )
        )

        db.commit()

        db.close()

        return render(
            request,
            "create_task.html",
            {
                "message":
                "Task Created Successfully"
            }
        )

    return render(
        request,
        "create_task.html"
    )


@api_view(["POST"])
def view_task(request):

    if request.method == "POST":

        db = db_con()
        cu = db.cursor()

        name = request.POST.get(
            "name"
        )

        phone_num = request.POST.get(
            "phone_num"
        )

        cu.execute(
            """
            SELECT title,
                   description
            FROM users
            WHERE phone_num=%s
            AND name=%s
            """,
            (
                phone_num,
                name
            )
        )

        task = cu.fetchone()

        db.close()

        if task:

            return render(
                request,
                "view_task.html",
                {
                    "title": task[0],
                    "description": task[1]
                }
            )

        return render(
            request,
            "view_task.html",
            {
                "message":
                "Task Not Found"
            }
        )

    return render(
        request,
        "view_task.html"
    )
@api_view(["POST"])
def update_task(request):

    if request.method == "POST":

        db = db_con()
        cu = db.cursor()

        name = request.POST.get(
            "name"
        )

        phone_num = request.POST.get(
            "phone_num"
        )

        title = request.POST.get(
            "title"
        )

        description = request.POST.get(
            "description"
        )

        cu.execute(
            """
            UPDATE users
            SET title=%s,
                description=%s
            WHERE name=%s
            AND phone_num=%s
            """,
            (
                title,
                description,
                name,
                phone_num
            )
        )

        db.commit()

        db.close()

        return render(
            request,
            "update_task.html",
            {
                "message":
                "Task Updated Successfully"
            }
        )

    return render(
        request,
        "update_task.html"
    )

@api_view(["POST"])
def delete_task(request):

    if request.method == "POST":

        db = db_con()
        cu = db.cursor()

        name = request.POST.get(
            "name"
        )

        phone_num = request.POST.get(
            "phone_num"
        )

        cu.execute(
            """
            UPDATE users
            SET title=%s,
                description=%s
            WHERE name=%s
            AND phone_num=%s
            """,
            (
                "NO TITLE",
                "NO DESCRIPTION",
                name,
                phone_num
            )
        )

        db.commit()

        db.close()

        return render(
            request,
            "delete_task.html",
            {
                "message":
                "Task Deleted Successfully"
            }
        )

    return render(
        request,
        "delete_task.html"
    )
    # -------- ADMIN SIGNUP --------

@api_view(["POST"])
def admin_signup(request):

    if request.method == "POST":

        db = db_con()
        cu = db.cursor()

        name = request.POST.get(
            "name"
        )

        pin = request.POST.get(
            "pin"
        )

        password = request.POST.get(
            "password"
        )

        re_password = request.POST.get(
            "re_password"
        )

        if password != re_password:

            return render(
                request,
                "admin_signup.html",
                {
                    "message":
                    "Passwords do not match"
                }
            )
        pin = request.POST.get("pin")

        if not pin:

            return render(
            request,
        "admin_signup.html",
        {
            "message":
            "Pin is required"
        }
    )

        if not pin.isdigit():

            return render(
        request,
        "admin_signup.html",
        {
            "message":
            "Pin must contain numbers only"
        }
    )
        cu.execute(
            """
            SELECT *
            FROM admins
            WHERE name=%s
            AND pin=%s
            """,
            (
                name,
                pin
            )
        )

        admin = cu.fetchone()

        if admin:

            return render(
                request,
                "admin_signup.html",
                {
                    "message":
                    "Admin Already Exists"
                }
            )

        hashed_password = make_password(
            password
        )

        cu.execute(
            """
            INSERT INTO admins
            (name,pin,password)
            VALUES (%s,%s,%s)
            """,
            (
                name,
                pin,
                hashed_password
            )
        )

        db.commit()

        db.close()

        return redirect(
            "/admin-login-page"
        )

    return render(
        request,
        "admin_signup.html"
    )


@api_view(["POST"])
def admin_login(request):

    if request.method == "POST":

        db = db_con()
        cu = db.cursor()

        name = request.POST.get(
            "name"
        )

        pin = request.POST.get(
            "pin"
        )

        password = request.POST.get(
            "password"
        )
        

        cu.execute(
            """
            SELECT password
            FROM admins
            WHERE name=%s
            AND pin=%s
            """,
            (
                name,
                pin
            )
        )

        admin = cu.fetchone()

        if admin:

            stored_password = admin[0]

            if check_password(
                password,
                stored_password
            ):

                db.close()

                return redirect(
                    "/admin-main-page"
                )

            else:

                db.close()

                return render(
                    request,
                    "admin_login.html",
                    {
                        "message":
                        "Wrong Password"
                    }
                )

        db.close()

        return render(
            request,
            "admin_login.html",
            {
                "message":
                "Admin Not Found"
            }
        )

    return render(
        request,
        "admin_login.html"
    )


def all_users(request):

    db = db_con()
    cu = db.cursor()

    cu.execute(
        """
        SELECT id,
               name,
               phone_num
        FROM users
        """
    )

    users = cu.fetchall()

    db.close()

    return render(
        request,
        "admin_all_users.html",
        {
            "users": users
        }
    )

@api_view(["GET"])
def all_tasks(request):

    db = db_con()
    cu = db.cursor()

    cu.execute(
        """
        SELECT id,
               name,
               title,
               description
        FROM users
        """
    )

    tasks = cu.fetchall()

    db.close()

    return render(
        request,
        "admin_all_tasks.html",
        {
            "tasks": tasks
        }
    )


def delete_task_admin(request):

    if request.method == "POST":

        db = db_con()
        cu = db.cursor()

        user_id = request.POST.get(
            "user_id"
        )

        print(user_id)

        cu.execute(
            """
            UPDATE users
            SET title=%s,
                description=%s
            WHERE id=%s
            """,
            (
                "NO TITLE",
                "NO DESCRIPTION",
                user_id
            )
        )

        db.commit()

        print(cu.rowcount)

        db.close()

        if cu.rowcount > 0:

            return render(
                request,
                "admin_delete_tasks.html",
                {
                    "message":
                    "Task Deleted Successfully"
                }
            )

        return render(
            request,
            "admin_delete_tasks.html",
            {
                "message":
                "User Not Found"
            }
        )

    return render(
        request,
        "admin_delete_tasks.html"
    )