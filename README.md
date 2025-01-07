# 📝 Blog Management System

## 📌 Overview  
The **Blog Management System** is a Django-based RESTful API that allows users to register, log in, create blog posts, and comment on posts. The system uses **Django REST Framework (DRF)** for API development and **Token-based authentication** for secure user sessions.

---

## 🚀 Features  
✅ User authentication (registration, login, logout)  
✅ Token-based authentication for secure access  
✅ CRUD operations for blog posts  
✅ Commenting system for blog posts  
✅ Token-based authentication for API access  

---

## 🏗️ Technologies Used  
- **Python** (Django & DRF)  
- **SQLite** (Database)  
- **Django REST Framework (DRF)**  
- **Token Authentication**  
- **Git & GitHub**  

---

## 🛠️ Installation  

### 🔹 Step 1: Clone the Repository  
```sh
git clone https://github.com/aggarwal-shruti/Blog_management_system.git
cd Blog_management_system
```


### 🔹 Step 2: Create a Virtual Environment  
```sh
python -m venv venv
venv\Scripts\activate     # For Windows
```
### 🔹 Step 3: Install Dependencies 
```sh
pip install -r requirements.txt
```
### 🔹 Step 4: Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```
### 🔹 Step 5: Run Server
```sh
python manage.py runserver
```
The API will be available at: http://127.0.0.1:8000/api/

## 📌 API Endpoints
### 🔹 User Authentication
```sh
Method	Endpoint	Description
POST	/api/register/	Register a new user
POST	/api/login/	Log in a user
POST	/api/logout/	Log out a user
POST	/api/token/	Obtain authentication token
```
### 🔹 Blog Management
```sh
Method	Endpoint	Description
GET	/api/blogs/  	List all blogs
POST	/api/blogs/	 Create a new blog
GET	/api/blogs/{id}/	Retrieve a blog by ID
PUT	/api/blogs/{id}/	Update a blog
DELETE	/api/blogs/{id}/	Delete a blog
```
## 🔹 Comments
```sh
Method	Endpoint	Description
GET	/api/comment/	List all comments
POST	/api/comment/	Add a new comment
```

