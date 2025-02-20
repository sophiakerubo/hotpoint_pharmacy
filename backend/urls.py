"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from pharmacy.views import ProductViewSet, test_view
from django.http import HttpResponse

# Initialize router for ViewSets
router = DefaultRouter()
router.register(r'products', ProductViewSet)

# Define home view
def home(request):
    return HttpResponse("Welcome to Hotpoint Pharmacy!")

# Final urlpatterns list (merged)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('api/auth/', include('authentication.urls')),  # Ensure 'authentication' app exists and has a urls.py file
    path('api/', include(router.urls)),  # Include DRF router URLs
    path('api/test/', test_view, name='test-view'),
    path('api/', include('products.urls')),
]