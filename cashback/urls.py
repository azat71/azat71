from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/cashback/division', CashBackApiView.as_view()),
    path('api/v1/cashback/addition', CashAddApiView.as_view())
]