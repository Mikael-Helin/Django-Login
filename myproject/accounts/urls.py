from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('public/', views.public_page, name='public'),
    path('private/', views.private_page, name='private'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]