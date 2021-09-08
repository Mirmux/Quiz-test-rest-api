"""rest_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='Quiz Test',
        description='Simple Test Project API',
        default_version='1.0.0',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='mirfayziyev5@gmail.com'),
        license=openapi.License(name='akfa_slash_license'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,
                        )
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # for CRUD rest  api
    # path('', include(router.urls)),

    # for auth django rest framework
    path('api/v1/auth', include('rest_framework.urls')),
    # path('api/v1/dj_rest_auth/', include('dj_rest_auth.urls')),
    # path('api/v1/dj_rest_auth/registration', include('dj_rest_auth.registration.urls')),
    # path('api/allauth/', include('allauth.urls')),

    # include apps urls
    path('api/', include('api.urls')),
    path('api/accounts/', include('accounts.urls')),


    # swagger UI
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0),name='schema_swagger_ui'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema_redoc'),




]
