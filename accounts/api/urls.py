from django.urls import path, include
# from rest_framework import routers

from knox.views import LogoutView

from .views import UserAPIView, RegisterAPIView, LoginAPIView, UserViewSet

# router = routers.DefaultRouter()
# router.register('users', UserViewSet, 'users')


urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout'),
    path('users', UserViewSet.as_view({
        'get': 'list'
    }), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({
        'get': 'retrieve'
    }), name='user-detail')
]
# urlpatterns += router.urls
print('users api urls ======>', urlpatterns)