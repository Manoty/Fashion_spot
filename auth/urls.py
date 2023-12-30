from django.urls import path
from . import views as my_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', my_views.register, name='registration-url'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login-url'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout-url')
]