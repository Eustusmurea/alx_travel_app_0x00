📌 About the Project
alxtravelapp is a real-world Django application designed as the foundation for a travel listing platform.

This milestone focuses on:

Setting up the initial project structure

Configuring a robust MySQL database

Integrating tools for automated API documentation

Ensuring maintainable, production-ready configurations

The goal is to equip learners with industry-standard best practices for starting and managing Django-based projects in a scalable and team-friendly way.

🎯 Learning Objectives
As a professional developer, by completing this milestone you will:

✅ Master Advanced Project Initialization
Bootstrap Django projects with modular, production-ready configurations

Use environment variables for secure, scalable settings

✅ Integrate Key Developer Tools
Set up Swagger (via drf-yasg) for automated API documentation

Implement CORS headers and configure MySQL for robust API interactions

✅ Collaborate Effectively Using Git
Structure projects for seamless team collaboration with version control

✅ Adopt Industry Best Practices
Manage dependencies, database configurations, and app structure in a maintainable way

⚙️ Requirements
Before starting, ensure you have:

Familiarity with Django and Django REST Framework

Knowledge of MySQL and basic database management

Understanding of Git for version control

A basic grasp of environment variable management with django-environ

🌟 Key Highlights
📌 Project Initialization
Create a Django project named alxtravelapp

Add an app named listings to encapsulate core functionalities

📌 Dependency Management
Install essential packages:

django: Core web framework

djangorestframework: For building REST APIs

django-cors-headers: CORS configuration

drf-yasg: Swagger API documentation

django-environ: Environment variable management

celery and rabbitmq: For future background task processing

📌 Settings Configuration
Use django-environ to handle environment variables via .env files

Configure MySQL as the primary database

Set up the Django REST Framework and CORS headers

📌 Swagger Integration
Integrate Swagger using drf-yasg for automated, comprehensive API documentation

Expose documentation at /swagger/