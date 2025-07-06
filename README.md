# alxtravelapp

alxtravelapp is a Django-based backend project designed as the foundation for a scalable travel listing platform. This repository demonstrates industry-standard best practices for initializing, configuring, and documenting a modern Django REST API, with a focus on maintainability, security, and team collaboration.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Version Control](#version-control)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

alxtravelapp serves as a robust backend for a travel listing platform. The project is structured to support future enhancements, including advanced API features, background task processing, and seamless team collaboration. The initial milestone covers project setup, secure configuration, MySQL integration, and automated API documentation using Swagger.

---

## Features

- **Modular Django Project Structure**
- **MySQL Database Integration**
- **RESTful API with Django REST Framework**
- **Automated API Documentation with Swagger (drf-yasg)**
- **CORS Support for Cross-Origin Requests**
- **Environment Variable Management with django-environ**
- **Ready for Background Task Processing (Celery & RabbitMQ)**
- **Version Control with Git**

---

## Learning Objectives

By working through this project, you will:

- **Master Advanced Project Initialization**
    - Bootstrap Django projects with modular, production-ready configurations.
    - Securely manage environment variables for scalable deployments.
- **Integrate Key Developer Tools**
    - Set up Swagger (drf-yasg) for automated API documentation.
    - Implement CORS headers and configure MySQL for robust API interactions.
- **Collaborate Effectively Using Git**
    - Structure your project for seamless team collaboration and version control.
- **Adopt Industry Best Practices**
    - Manage dependencies, database configurations, and application structure following professional standards.

---

## Requirements

Before you begin, ensure you have:

- Python 3.8+
- Django 4.x
- MySQL Server
- [pip](https://pip.pypa.io/en/stable/)
- [Git](https://git-scm.com/)
- Basic knowledge of:
    - Django & Django REST Framework
    - MySQL database management
    - Version control with Git
    - Environment variable management (django-environ)

---

## Project Structure

```
alxtravelapp/
├── listings/                # Core app for travel listings
├── alxtravelapp/            # Project settings and configuration
├── requirements.txt         # Python dependencies
├── .env.example             # Example environment variables
├── manage.py
└── README.md
```

---

## Installation

1. **Clone the repository:**
     ```bash
     git clone https://github.com/yourusername/alxtravelapp.git
     cd alxtravelapp
     ```

2. **Create and activate a virtual environment:**
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate

     # using pipenv
     pip install pipenv
     pipenv shell
     ```

3. **Install dependencies:**
     ```bash
     pip install -r requirements.txt
     ```

4. **Set up environment variables:**
     - Copy `.env.example` to `.env` and update values as needed.

5. **Configure MySQL database:**
     - Ensure MySQL is running and create a database for the project.
     - Update `.env` with your database credentials.

6. **Apply migrations:**
     ```bash
     python manage.py migrate
     ```

---

## Configuration

- **Environment Variables:**
    Managed using `django-environ`. Store sensitive settings (e.g., `SECRET_KEY`, database credentials) in the `.env` file.
- **Database:**
    Configured for MySQL in `settings.py` using environment variables.
- **CORS:**
    Enabled via `django-cors-headers` for secure cross-origin API access.
- **API Documentation:**
    Swagger UI available at `/swagger/` (powered by `drf-yasg`).

---

## Running the Application

```bash
python manage.py runserver
```

- The API will be available at `http://localhost:8000/`
- Swagger documentation: `http://localhost:8000/swagger/`

---

## API Documentation

Interactive API docs are auto-generated using Swagger (drf-yasg).
Visit: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

---

## Version Control

- The project uses Git for version control.
- All setup files and configurations are committed.
- Push your changes to a GitHub repository named `alxtravelapp`.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License.

---