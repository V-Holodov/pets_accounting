from django.contrib import admin
from django.urls import include, path
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


schema_view = get_schema_view(title='Pets API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("docs/", schema_view, name="docs"),
]
