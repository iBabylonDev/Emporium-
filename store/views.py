from django.shortcuts import get_object_or_404, render

from .models import Category, Product

def product_detail(request, slug):
  product = get_object_or_404(Product.products, slug=slug, in_stock=True)
  return render(request, 'store/single.html', {'product': product})

def product_all(request):
    products = Product.products.all()
    return render(request, 'store/index.html', {'products': products})

def categories(request):
    return {
        'categories': Category.objects.all()
    }
def category_list(request, category_slug=None):
  category = get_object_or_404(Category, slug=category_slug)
  products = Product.objects.filter(category=category)
  return render(request, 'store/category.html', {'category': category, 'products': products})