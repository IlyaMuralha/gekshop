from django.shortcuts import HttpResponseRedirect, get_object_or_404

from mainapp.models import Product
from basket.models import Basket

def basket_add(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)

