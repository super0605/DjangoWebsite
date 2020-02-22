from django.urls import path

from .views import index, TodoDetailView, AccountsDetailView

urlpatterns = [
    path('', index),
    path('login', index),
    path('register', index),
    path('edit/<int:pk>', TodoDetailView.as_view()),
    path('delete/<int:pk>', TodoDetailView.as_view()),
    path('accounts', index),
    path('accounts/<int:pk>', AccountsDetailView.as_view()),
]
