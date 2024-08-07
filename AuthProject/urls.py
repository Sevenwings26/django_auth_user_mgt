from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authapp.urls")),
    # To use prewritten template from authentication suuc as login and register.
    path("", include('django.contrib.auth.urls')),
    
    # Using django views
    # path("password-reset/", PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),

    # path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
