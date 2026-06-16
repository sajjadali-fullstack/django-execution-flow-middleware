# Django Middleware Demos

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![Middleware](https://img.shields.io/badge/Topic-Middleware-orange)

## 📖 Overview

This repo demonstrates two real-world Django custom middleware patterns — how middleware participates in the request-response lifecycle, blocks requests during maintenance, and how initialization, pre-processing, view execution, and post-processing all connect together.

---

## 📁 Project Structure

```
django-middleware-demos/
├── execution_flow/
│   ├── middleware.py       # ExecutionFlowMiddleware — logs request lifecycle
│   ├── views.py            # welcome_view — returns styled HTML response
│   ├── urls.py             # URL routing
│   └── settings.py         # MIDDLEWARE list config
│
└── maintenance_mode/
    ├── middleware.py       # AppMaintenanceMiddleware — blocks all requests
    ├── views.py            # home_page — blocked during maintenance
    └── urls.py             # URL routing
```

---

## 🔁 Project 1 — Execution Flow Middleware

Shows how Django middleware wraps around every request-response cycle.

```
Server starts
    └── Middleware.__init__()           ← runs once at startup
         └── Request received
              └── Middleware.__call__() — pre-processing
                   └── View function executes
                        └── Middleware.__call__() — post-processing
                             └── Response returned
```

### 🧠 Key Concepts

| Method | When it runs |
|--------|-------------|
| `__init__` | Once — when the server starts |
| `__call__` (before `get_response`) | Every request — pre-processing |
| `get_response(request)` | Calls the actual view |
| `__call__` (after `get_response`) | Every request — post-processing |

### ⚙️ Register in `settings.py`

```python
MIDDLEWARE = [
    ...
    'execution_flow.middleware.ExecutionFlowMiddleware',
]
```

---

## 🚧 Project 2 — Maintenance Mode Middleware

Shows how middleware can short-circuit the request pipeline entirely — the view function never executes.

```
Request received
    └── AppMaintenanceMiddleware.__call__()
         └── Returns maintenance HttpResponse directly
              └── View is never called
```

### 🧠 Key Concepts

| Behavior | How it works |
|----------|-------------|
| Blocks all routes | `__call__` returns response before `get_response` is called |
| View never runs | No `self.get_response(request)` call |
| Easy to toggle | Comment out middleware in `settings.py` to restore normal flow |

### ⚙️ Register in `settings.py`

```python
MIDDLEWARE = [
    ...
    'maintenance_mode.middleware.AppMaintenanceMiddleware',
]
```

---

## ⚙️ Setup

```bash
git clone https://github.com/your-username/django-middleware-demos
cd django-middleware-demos
pip install django
python manage.py runserver
```

---

## 👨‍💻 Author

**Sajjad Ali**

Python Full Stack Developer

Building Django projects while exploring backend architecture and middleware concepts.

## 📄 License

MIT
