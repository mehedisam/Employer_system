# Employer Management System API

This project is a simple RESTful API built with Django REST Framework to manage Employers. It features a custom user authentication system using email and JWT tokens.

## 🔧 Features

- Custom User model (email-based login)
- JWT Authentication with Simple JWT
- Employer CRUD operations
- Swagger API Documentation

## 📁 Folder Structure

```
employer_mgmt_api/
│
├── employer_mgmt_api/        # Django project settings
├── api/                      # App containing models, views, serializers
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional)

### Installation

1. **Clone the repository or extract the ZIP**
```bash
git clone <repo-url>  # or extract employer_mgmt_api.zip
cd employer_mgmt_api
```

2. **Create and activate a virtual environment**
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Run the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/swagger/` to access the Swagger API documentation.

## 🔐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/auth/signup/` | Register a new user |
| POST   | `/api/auth/login/` | Login and get JWT tokens |
| GET    | `/api/auth/profile/` | Retrieve the authenticated user's profile |
| POST   | `/api/employers/` | Create a new employer |
| GET    | `/api/employers/` | List all employers for the authenticated user |
| GET    | `/api/employers/<id>/` | Retrieve a single employer |
| PUT    | `/api/employers/<id>/` | Update an employer |
| DELETE | `/api/employers/<id>/` | Delete an employer |

**🔒 Note:** All `/api/employers/` endpoints require authentication.

## ✅ Authentication

This project uses JWT (JSON Web Tokens) for securing endpoints. After logging in, you’ll receive access and refresh tokens.

Include the access token in the `Authorization` header for protected routes:

```
Authorization: Bearer <access_token>
```

## 📄 License

This project is licensed for educational purposes.
