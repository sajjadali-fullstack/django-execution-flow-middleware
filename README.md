# django-execution-flow-middleware
## # Django Execution Flow Middleware

## 📖 Overview

This project demonstrates how Django custom middleware participates in the request-response lifecycle. It shows middleware initialization, request pre-processing, view execution, and response post-processing using a simple function-based view.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![Middleware](https://img.shields.io/badge/Topic-Middleware-orange)

A minimal Django project demonstrating how **custom middleware** intercepts every HTTP request and response in the WSGI pipeline.

## 🔁 Execution Flow

```
Server starts
    └── Middleware.__init__()       ← runs once at startup
         └── Request received
              └── Middleware.__call__() — pre-processing
                   └── View function executes
                        └── Middleware.__call__() — post-processing
                             └── Response returned
```

## 📁 Project Structure

```
project/
├── middleware.py       # Custom ExecutionFlowMiddleware
├── views.py            # welcome_view — returns styled HTML response
├── urls.py             # URL routing
└── settings.py         # MIDDLEWARE list config
```

## ⚙️ Setup

```bash
git clone https://github.com/your-username/django-execution-flow-middleware
cd django-execution-flow-middleware
pip install django
python manage.py runserver
```

Register middleware in `settings.py`:
```python
MIDDLEWARE = [
    ...
    'yourapp.middleware.ExecutionFlowMiddleware',
]
```

## 🧠 Key Concepts

| Method | When it runs |
|--------|-------------|
| `__init__` | Once — when the server starts |
| `__call__` (before `get_response`) | Every request — pre-processing |
| `get_response(request)` | Calls the actual view |
| `__call__` (after `get_response`) | Every request — post-processing |

## 👨‍💻 Author

Senior Full Stack Python Developer  
Built as part of Django middleware deep-dive series.

## 📄 License

MIT
