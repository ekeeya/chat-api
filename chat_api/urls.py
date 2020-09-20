
from django.contrib import admin
from django.urls import path, include

# Url patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat', include('chat.urls')),
]
