from django.urls import path
from sale.views import *


urlpatterns = [
    path('api/v1/list/sale', SaleListApiView.as_view()),
    path('api/v1/create/sale', SaleCreateAPIView.as_view()),
    path('api/v1/update_sale/<int:pk>/', SaleUpdateAPIView.as_view()),
    path('api/v1/destroy_sale/<int:pk>/', SaleDestroyAPIView.as_view()),

    path('api/v1/list/sale_product', SaleProductListApiView.as_view()),
    path('api/v1/create/sale_product', SaleProductCreateAPIView.as_view()),
    path('api/v1/update_sale_product/<int:pk>/', SaleProductUpdateAPIView.as_view()),
    path('api/v1/destroy_sale_product/<int:pk>/', SaleProductDestroyAPIView.as_view()),

]