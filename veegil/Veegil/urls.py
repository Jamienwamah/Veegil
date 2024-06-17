"""
URL configuration for Veegil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Basic Bank API",
        default_version='v1',
        description="This is a basic bank rest apis  that is being fed to the next js. This api helps users to easily access the appilcation\n and explore different features the application has to offer.",
        terms_of_service="https://ik-portfolio.vercel.app",
        contact=openapi.Contact(email="ikechukwuarinze614@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('deposit.urls')),
    path('api/v1/', include('otp.urls')),
    path('api/v1/', include('signin.urls')), 
    path('api/v1/', include('signup.urls')),
    path('api/v1/', include('transactions.urls')),
    path('api/v1/', include('transfer.urls')),
    path('api/v1/', include('balance.urls')),
    path('api/v1/', include('profiles.urls')),
    path('api/v1/', include('withdraw.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name = 'schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
