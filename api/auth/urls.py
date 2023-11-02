from .views import LoginView, LogoutView, RegisterView
from django.urls import path

urlpatterns = [
    path('login', LoginView.as_view(), name='api-login'),
    path('logout', LogoutView.as_view(), name='api-logout'),
    path('register', RegisterView.as_view(), name='api-register'),

]
