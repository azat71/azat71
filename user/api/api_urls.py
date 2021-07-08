from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user.api.api_view import (
    registration_view,
)

app_name = 'user'
urlpatterns = [
    path('register', registration_view, name='register'),
    path('auth', obtain_auth_token, name='auth'),

]
