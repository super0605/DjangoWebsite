"""
todocrud URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('', include('frontend.urls')),
    path('api/', include('todos.api.urls')),
    path('admin/', admin.site.urls),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
]
