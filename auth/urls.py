from django.urls import path, include
from . import views as my_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', my_views.register, name='registration-url'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login-url'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout-url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

]