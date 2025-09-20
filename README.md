# Cafe Web App

A dynamic cafe website built with Django, HTML, CSS, and JavaScript.

## Features

- Home page with hero section and features
- Dynamic menu with category filtering
- Gallery page with image modal functionality
- About page
- Contact page with form
- Admin panel for content management
- Responsive design

## Setup Instructions

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create superuser:
   ```
   python manage.py createsuperuser
   ```

4. Run development server:
   ```
   python manage.py runserver
   ```

## Project Structure

```
cafe_webapp/
├── cafe_project/          # Django project settings
├── cafe/                  # Main app
├── templates/cafe/        # HTML templates
├── static/               # CSS, JS, Images
├── media/                # User uploads
└── requirements.txt      # Dependencies
```

## Pages

- `/` - Home page
- `/menu/` - Menu page
- `/gallery/` - Gallery page
- `/about/` - About page
- `/contact/` - Contact page
- `/admin/` - Admin panel