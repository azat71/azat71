
from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/list/product', ProductListApiView.as_view()),
    path('api/v1/create/product', ProductCreateAPIView.as_view()),
    path('api/v1/update_product/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('api/v1/destroy_product/<int:pk>/', ProductDestroyAPIView.as_view()),

    path('api/v1/list/product_type', TypeProductListApiView.as_view()),
    path('api/v1/create/product_type', TypeProductCreateAPIView.as_view()),
    path('api/v1/update_product_type/<int:pk>/', TypeProductUpdateAPIView.as_view()),
    path('api/v1/destroy_product_type/<int:pk>/', TypeProductDestroyAPIView.as_view()),

    path('api/v1/create/category/', CategoryCreateAPIView.as_view()),
    path('api/v1/update/<int:pk>/', CategoryUpdateAPIView.as_view()),
    path('api/v1/destroy/<int:pk>/', CategoryDestroyAPIView.as_view()),

]