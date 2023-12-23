from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Product

# Create your views here.


def fir(request):
    return render(request, "index.html")


def ind(request):
    return render(request, "souq/index.html")

