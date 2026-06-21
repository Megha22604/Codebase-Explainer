# 🧭 Codebase Onboarding Guide

> **Repo:** [https://github.com/Megha22604/packaging-box-calculator](https://github.com/Megha22604/packaging-box-calculator)
> **Generated:** 2026-06-20

---

## 📌 PROJECT SUMMARY

This project is a modern dark-themed web application built with Django and OpenCV that enables users to upload product images. It automatically detects product dimensions from these images, calculates the optimal packaging box size with padding, and estimates the associated cost. The UI is designed for a sleek dashboard experience using Bootstrap 5 and custom CSS.

---

## 🧰 TECH STACK

- Django
- OpenCV
- Python
- Bootstrap 5
- Bootstrap Icons
- Lovable (AI tool)
- Claude (AI tool)
- DesignArena (AI tool)
- Copilot (Microsoft)

---

## 📁 FILE BREAKDOWN

- **AI_USAGE.md**: Documents the various AI tools (Lovable, Claude, DesignArena, Copilot) used during the project's development for tasks like brainstorming, clarification, UI suggestions, and code generation.
- **README.md**: Provides a high-level overview of the project, its core functionality (packaging box calculation, dimension detection), and key features like the dark theme UI.
- **TEST_CASES.md**: Outlines specific manual test scenarios for different aspects of the application, such as image upload, error handling for missing/invalid images, and cost calculation verification.
- **TEST_OUTPUT.md**: A concise file indicating that all defined tests passed successfully.
- **manage.py**: Django's command-line utility, used for various administrative tasks like running the development server, performing database migrations, and more.
- **packaging_app/asgi.py**: Configuration for the ASGI (Asynchronous Server Gateway Interface) server, used for asynchronous Python web applications.
- **packaging_app/settings.py**: The main configuration file for the Django project, where database settings, installed apps, static file paths, and other project-wide settings are defined.
- **packaging_app/urls.py**: The project's root URL configuration, which routes incoming web requests to the appropriate views within the application.
- **packaging_app/wsgi.py**: Configuration for the WSGI (Web Server Gateway Interface) server, commonly used for synchronous Python web applications.
- **products/admin.py**: Registers models with the Django administration site, allowing CRUD operations on `Product` instances through an intuitive web interface.
- **products/apps.py**: Configuration for the `products` Django app, defining its name and other app-specific settings.
- **products/forms.py**: Defines a `ModelForm` for the `Product` model, which facilitates handling user input for creating or updating product entries.
- **products/migrations/0001_initial.py**: The first database migration script for the `products` app, creating the initial `Product` model with fields like name, image, and placeholder dimensions.
- **products/migrations/0002_remove_product_height_remove_product_length_and_more.py**: A subsequent migration that removes dimension-related fields (height, length, weight, etc.) from the `Product` model, indicating that these are now dynamically calculated.
- **products/models.py**: Defines the `Product` database model and contains the core OpenCV logic within the `get_dimensions` method to process uploaded images, detect contours, and calculate product length and width.
- **products/static/css/style.css**: Custom CSS rules for styling the web application, particularly focusing on the dark theme, sidebar navigation, and card components to achieve the desired UI aesthetic.
- **products/templates/results.html**: An HTML template responsible for displaying the calculated packaging box dimensions and estimated cost to the user after an image has been processed.

---

## 🚀 HOW TO START

1.  **Clone the repository**: Use `git clone [repository-url]` to get the project files onto your local machine.
2.  **Set up a virtual environment and install dependencies**: Navigate to the project root, create a virtual environment (`python -m venv venv`), activate it (`source venv/bin/activate` on Linux/macOS or `venv\Scripts\activate` on Windows), and install necessary packages (e.g., `pip install django opencv-python`).
3.  **Run database migrations**: Once dependencies are installed, apply the database schema changes by running `python manage.py makemigrations products` and then `python manage.py migrate`.
4.  **Start the development server**: Execute `python manage.py runserver` from the project root. The application should then be accessible in your web browser, typically at `http://127.0.0.1:8000/`.

---

## ⚠️ GOTCHAS

-   **OpenCV Installation**: Integrating `opencv-python` can sometimes require system-level dependencies or specific build tools, so be prepared for potential installation hurdles beyond `pip install`.
-   **Incomplete Core Files**: The provided snippets for `packaging_app/settings.py` and `packaging_app/urls.py` appear incomplete. You will need to complete essential Django configurations such as adding `products` to `INSTALLED_APPS`, defining `MEDIA_URL` and `MEDIA_ROOT`, and including `products.urls` in the main `urlpatterns`.
-   **`manage.py` Truncation**: The `manage.py` file snippet is cut off at `execute`. It should be `execute_from_command_line(sys.argv)` to be functional.
-   **Missing Views**: There is no `products/views.py` file provided. The logic for handling form submissions, uploading images, calling the OpenCV dimension detection, and rendering the results (`results.html`) will need to be implemented within a `views.py` file and mapped in `products/urls.py`.
-   **Dimension Calibration**: The `pixel_to_cm = 0.1` factor in `products/models.py` is crucial for accurate dimension calculation. This value likely requires careful calibration based on the specific camera setup and distances used when capturing product images.

---
