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



    
###postman repository
{
  "info": {
    "_postman_id": "85c0721d-9ddd-4c00-8e5e-3336c5ef96ae",
    "name": "primetrade_ass",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    "_exporter_id": "47633912",
    "_collection_link": "https://go.postman.co/collection/47633912-85c0721d-9ddd-4c00-8e5e-3336c5ef96ae?source=collection_link"
  },
  "item": [
    {
      "name": "user_signup",
      "protocolProfileBehavior": {
        "disableBodyPruning": true
      },
      "request": {
        "method": "OPTIONS",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"name\":\"sagar\",\r\n    \"phone_num\":\"9999999999\",\r\n    \"password\":\"1234\",\r\n    \"re_password\":\"1234\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://127.0.0.1:8000/signup",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "signup"
          ]
        }
      },
      "response": []
    },
    {
      "name": "user_login",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"name\":\"sagar\",\r\n    \"phone_num\":\"9999999999\",\r\n    \"password\":\"1234\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://127.0.0.1:8000/login",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "login"
          ]
        }
      },
      "response": []
    },
    {
      "name": "User_create_task",
      "protocolProfileBehavior": {
        "disableBodyPruning": true
      },
      "request": {
        "method": "OPTIONS",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"name\":\"sagar\",\r\n    \"phone_num\":\"9999999999\",\r\n    \"title\":\"djNgo\",\r\n    \"description\":\"not\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://127.0.0.1:8000/create-task",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "create-task"
          ]
        }
      },
      "response": []
    },
    {
      "name": "user_view_task",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"name\":\"sagar\",\r\n    \"phone_num\":\"9999999999\"\r\n   \r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://127.0.0.1:8000/view-task",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "view-task"
          ]
        }
      },
      "response": []
    },
    {
      "name": "user_delete_task",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"name\":\"sagar\",\r\n    \"phone_num\":\"9999999999\"\r\n   \r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://127.0.0.1:8000/delete-task",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "delete-task"
          ]
        }
      },
      "response": []
    },
    {
      "name": "user_updat_task",
      "protocolProfileBehavior": {
        "disableBodyPruning": true
      },
      "request": {
        "method": "OPTIONS",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"name\":\"sagar\",\r\n    \"phone_num\":\"9999999999\",\r\n    \"title\":\"Python\",\r\n    \"description\":\"Backend API\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://127.0.0.1:8000/update-task",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "update-task"
          ]
        }
      },
      "response": []
    },
    {
      "name": "admin_signup",
      "protocolProfileBehavior": {
        "disableBodyPruning": true
      },
      "request": {
        "method": "OPTIONS",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"name\":\"admin\",\r\n    \"pin\":\"99999\",\r\n    \"password\":\"1234\",\r\n    \"re_password\":\"1234\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://127.0.0.1:8000/admin-signup",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "admin-signup"
          ]
        }
      },
      "response": []
    },
    {
      "name": "admin_logn",
      "request": {
        "method": "POST",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"name\":\"admin\",\r\n    \"pin\":\"9999\",\r\n    \"password\":\"123\"\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://127.0.0.1:8000/admin-login",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "admin-login"
          ]
        }
      },
      "response": []
    },
    {
      "name": "admin_get_all_users",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:8000/all-users",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "all-users"
          ]
        }
      },
      "response": []
    },
    {
      "name": "all_tasks",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://127.0.0.1:8000/all-tasks",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "all-tasks"
          ]
        }
      },
      "response": []
    },
    {
      "name": "admin_delete_task",
      "protocolProfileBehavior": {
        "disableBodyPruning": true
      },
      "request": {
        "method": "OPTIONS",
        "header": [],
        "body": {
          "mode": "raw",
          "raw": "{\r\n    \"user_id\":1\r\n}",
          "options": {
            "raw": {
              "language": "json"
            }
          }
        },
        "url": {
          "raw": "http://127.0.0.1:8000/delete-task-admin",
          "protocol": "http",
          "host": [
            "127",
            "0",
            "0",
            "1"
          ],
          "port": "8000",
          "path": [
            "delete-task-admin"
          ]
        }
      },
      "response": []
    }
  ]
}