from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator
from shopping_cart.models import Order
from django.shortcuts import get_object_or_404


# Create your views here.
def product_list(request):
    title = None
    search = Product.objects.all()
    category = Category.objects.all()
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(ProName__icontains=title)

    ProductList = search

    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    # paginator = Paginator(ProductList, 7)  # Show 25 contacts per page.
    # Page = request.GET.get('page')
    # pro_list = paginator.get_page(Page)

    context = {'ProductList': ProductList,
               'object_list': object_list,
               'current_order_products': current_order_products,
               'category': category,
               }

    return render(request, 'Product/product_list.html', context)


def product_detiels(reques, slug):
    pro_detiels = Product.objects.get(ProSlug=slug)
    context = {'product_detieles': pro_detiels}
    return render(reques, 'Product/productDetiels.html', context)


def contactus(request):
    return render(request, 'contactus.html', context=None)
