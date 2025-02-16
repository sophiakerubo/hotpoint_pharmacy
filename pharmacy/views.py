from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
def test_view(request):
    return HttpResponse("Test View is working")