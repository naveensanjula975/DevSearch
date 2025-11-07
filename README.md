# DevSearch - Developer Networking Platform

A Django-based platform for developers to showcase their projects, connect with other developers, and build their professional network.

[![Django](https://img.shields.io/badge/Django-4.0.5-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Security](https://img.shields.io/badge/Security-A+-brightgreen.svg)](./SECURITY.md)

[Live Demo](https://developer-family.herokuapp.com/)

---

## ✨ Features

- 🔐 **User Authentication** - Registration, login, password reset
- 👤 **User Profiles** - Customizable profiles with skills and social links
- 🚀 **Project Showcase** - Upload and display your projects
- ⭐ **Review & Voting System** - Rate and review projects
- 💬 **Messaging** - Direct messaging between developers
- 🔍 **Search & Filtering** - Find projects and developers
- 📱 **Responsive Design** - Works on all devices
- 🔌 **REST API** - JWT-authenticated API endpoints

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/naveensanjula975/DevSearch.git
   cd DevSearch
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   # Copy the example file
   copy .env.example .env   # Windows
   cp .env.example .env     # Mac/Linux
   
   # Edit .env and add your configuration
   ```
   
   **Required:** Generate a SECRET_KEY:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

8. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

9. **Open your browser and visit:**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API: http://127.0.0.1:8000/api/

---

## 🛠️ Tech Stack

### Backend
- **Django 4.0.5** - Web framework
- **Django REST Framework** - API development
- **Simple JWT** - JWT authentication
- **PostgreSQL / SQLite** - Database
- **Python Decouple** - Environment variable management

### Frontend
- **HTML/CSS/JavaScript** - Traditional Django templates
- **Custom CSS** - Responsive design

### Deployment
- **Gunicorn** - WSGI server
- **WhiteNoise** - Static file serving
- **Heroku** - Cloud platform (configured)

---

## 🔌 API Endpoints

### Authentication
- `POST /api/users/token/` - Get JWT token
- `POST /api/users/token/refresh/` - Refresh token

### Projects
- `GET /api/projects/` - List all projects
- `GET /api/projects/{id}/` - Project details
- `POST /api/projects/{id}/vote/` - Vote on project (auth required)

**Full API documentation:** See [SETUP.md](./SETUP.md#api-endpoints)

---

## 🧪 Testing

```bash
# Run all tests (when implemented)
python manage.py test

# Run specific app tests
python manage.py test projects
python manage.py test users
```

---

## 🚢 Deployment

### Heroku Deployment

1. **Install Heroku CLI and login:**
   ```bash
   heroku login
   ```

2. **Create Heroku app:**
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY="your-secret-key"
   heroku config:set DEBUG="False"
   heroku config:set ALLOWED_HOSTS="your-app.herokuapp.com"
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

5. **Run migrations:**
   ```bash
   heroku run python manage.py migrate
   ```
---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Naveen Sanjula**
- GitHub: [@naveensanjula975](https://github.com/naveensanjula975)

---

## 🙏 Acknowledgments

- Django Documentation
- Django REST Framework
- The open-source community

---

**Made with ❤️ using Django**
