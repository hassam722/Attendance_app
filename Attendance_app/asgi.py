"""
ASGI config for Attendance_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
from venv import EnvBuilder
import os
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Attendance_app.settings')
django_asgi = get_asgi_application()

from Admin.consumer_admin import admin
from Employee.consumer import employee

application = ProtocolTypeRouter({
    # "http": some_app,
    "websocket": AuthMiddlewareStack(URLRouter([
                path("admin-app", admin.as_asgi()),
                path("employee-app", employee.as_asgi()),
            ])
        )
})
