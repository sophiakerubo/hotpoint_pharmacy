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
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from pharmacy.views import ProductViewSet, test_view # Import your pharmacy app
from django.urls import path, include

urlpatterns = [
    path('api/auth',
         include('auth.urls'))
]

router = DefaultRouter()
router.register(r'products', ProductViewSet)  # Replace 'items' with your model name

def home(request):
    return HttpResponse("Welcome to Hotpoint Pharmacy!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('api/', include(router.urls)),  # Ensure router has registered viewsets
  
   path('api/test/', test_view, name='test-view')
]