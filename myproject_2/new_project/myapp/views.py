
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Client, Product, Order


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
