from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/list/client', ClientListApiView.as_view()),
    path('api/v1/create/client', ClientCreateAPIView.as_view()),
    path('api/v1/update_client/<int:pk>/', ClientUpdateAPIView.as_view()),
    path('api/v1/destroy_client/<int:pk>/', ClientDestroyAPIView.as_view()),

]