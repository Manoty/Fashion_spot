from django.urls import path, include
from . import views as my_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('register/', my_views.register, name='registration-url'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login-url'),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout-url'),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    ]