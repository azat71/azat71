from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Feliz",
      default_version='v1',
      description="Test description",
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
   re_path(r'^(?P<format>\.json|\.yaml)/$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]