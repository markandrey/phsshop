from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from goods.models import Product


def catalog(request, category_slug):
    page = request.GET.get('page', 1)

    if category_slug == 'vse-tovary':
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    p = Paginator(goods, 3)
    current_page = p.page(int(page))

    context = {
        "title": "Home - каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):

    product = Product.objects.get(slug=product_slug)

    context = {
        "product": product,
    }

    return render(request, "goods/product.html", context)
