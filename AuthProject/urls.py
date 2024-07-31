from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authapp.urls")),
    # To use prewritten template from authentication suuc as login and register.
    path("", include('django.contrib.auth.urls')),
    
    # Using django views
    path("password-reset/", PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),

    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),


    # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    # path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
]
