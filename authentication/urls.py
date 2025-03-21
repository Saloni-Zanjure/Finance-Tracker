from .views import RegistrationView, UsernameValidationView, EmailValidationView, VerificationView,LoginView,LogoutView,RequestPasswordResetEmail,CompletePasswordReset,dashboard_view
from django.urls import path # type: ignore
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('dashboard_view', dashboard_view, name="dashboard_view"),
    path('login',LoginView.as_view(), name="login"),
    path('logout',LogoutView.as_view(), name="logout"),
    path('register',RegistrationView.as_view(), name="register"),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()),name="validate-user"),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()),name="validate-email"),
    path('activate/<uidb64>/<token>/',csrf_exempt(VerificationView.as_view()),name="activate"),
    path('request-reset-link',RequestPasswordResetEmail.as_view(),name="request-password"),
    path('set-new-password/<uidb64>/<token>/',CompletePasswordReset.as_view(),name="reset-user-password"),

]
