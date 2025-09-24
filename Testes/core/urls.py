from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('login/', views.user_login, name='login'),
]
