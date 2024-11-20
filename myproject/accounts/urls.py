from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_view, name='login'),
    path('public/', views.public_page, name='public'),
    path('private/', views.private_page, name='private'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('delete-image/', views.delete_image, name='delete_image'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)