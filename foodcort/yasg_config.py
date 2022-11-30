from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Food-court API",
        default_version='v1',
        description="API description",
        contact=openapi.Contact(email="contact@dummy.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
yasg_urls = [
    path(r'api/v1/playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'api/v1/docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
