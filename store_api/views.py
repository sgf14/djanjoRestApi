from django.shortcuts import render
from rest_framework import viewsets
from .models import product
from .serializers import ProductSerializer

# note this demo uses class approach vs function (def) approach.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = product.objects.all()

