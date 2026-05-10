Task Manager Django Project
Project Overview

This is a Django + MySQL Task Manager application with:

    User Signup/Login
    Create Task
    View Task
    Update Task
    Delete Task
    Admin Signup/Login
    View All Users
    View All Tasks
    Delete User Tasks


Technologies Used
    Python
    Django
    Django REST Framework
    MySQL
    HTML
    Render Deployment


Project Structure
    note_mage/
    │
    ├── manage.py
    ├── requirements.txt
    ├── Procfile
    ├── db.sqlite3
    │
    ├── not/
    │   ├── views.py
    │   ├── urls.py
    │   ├── db.py
    │   ├── templates/
    │
    └── note_mage/
        ├── settings.py
        ├── urls.py
        ├── wsgi.py


Features
    User Features
    User Signup
    User Login
    Create Task
    View Task
    Update Task
    Delete Task
Admin Features
    Admin Signup
    Admin Login
    View All Users
    View All Tasks
    Delete User Tasks

Database Tables

users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone_num VARCHAR(20),
    password VARCHAR(255),
    title VARCHAR(255),
    description TEXT
);

admins table
CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    pin INT,
    password VARCHAR(255)
);


Installation Steps
    Clone Repository
    git clone https://github.com/kollasagar18/task-manager.git

Move to Project Folder
    cd task-manager/note_mage
Install Packages
    pip install -r requirements.txt
Run Server
    python manage.py runserver




URL Endpoints
    User APIs
    Function	    URL
    User Signup	  =  /signup
    User Login	  =  /login
    Create Task	  =  /create-task
    View Task	  =  /view-task
    Update Task	  =  /update-task
    Delete Task	  =  /delete-task

Admin APIs
    Function	        URL
    Admin Signup	 =    /admin-signup
    Admin Login	     =    /admin-login
    All Users	     =    /all-users
    All Tasks	     =    /all-tasks
    Delete Task Admin =	/delete-task-admin

Template Pages
Page
    user_signup.html
    user_login.html
    user_main.html
    create_task.html
    view_task.html
    update_task.html
    delete_task.html
    admin_signup.html
    admin_login.html
    admin_main.html
    admin_all_users.html
    admin_all_tasks.html
    admin_delete_tasks.html


Deployment
    Render Deployment

Build Command
    pip install -r requirements.txt

Start Command
    gunicorn note_mage.wsgi:application
    requirements.txt
    Django==5.0.2
    djangorestframework==3.15.1
    gunicorn==21.2.0
    mysql-connector-python==9.4.0
    whitenoise==6.7.0
Procfile

    web: gunicorn note_mage.wsgi:application


GitHub Repository
    https://github.com/kollasagar18/task-manager.git

render repository
    https://task-manager-j82l.onrender.com

postman repository
    https://kollasagar-s2-5203529.postman.co/workspace/sagar-kolla's-Workspace~27fcf620-bf99-4a1a-8062-5f18b83ea3d2/run/47633912-72e48fb2-8981-4ddc-8142-1ba388b03f96?action=share&creator=47633912
