from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/list/branch', BranchListApiView.as_view()),
    path('api/v1create/branch', BranchCreateAPIView.as_view()),
    path('api/v1/update_branch/<int:pk>/', BranchUpdateAPIView.as_view()),
    path('api/v1/destroy_branch/<int:pk>/', BranchDestroyAPIView.as_view()),
]