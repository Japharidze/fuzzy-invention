from django.shortcuts import render, get_object_or_404

from .models import Product

def index(request):
    product_list = Product.objects.all()
    ctx = {
        "product_list": product_list,
    }

    return render(request, "index.html", ctx)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'detail.html', {'product': product})