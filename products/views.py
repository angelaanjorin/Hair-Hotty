from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Product, Category

# Create your views here.

def all_products(request):
    """" A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey ='lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products =products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn´t enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    products_count = products.count()
    products = products_pagination(request, products, 6)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'products_count': products_count,
        'search_term' : query,
        'current_categories' : categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def products_pagination(request, products, results):
    ''' Handles Pagination '''
    paginator = Paginator(products, results)
    page_number = request.GET.get('page')

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        page_number = 1
        products = paginator.page(page_number)
    except EmptyPage:
        page_number = paginator.num_pages
        products = paginator.page(page_number)

    return products


def product_detail(request, product_id):
    """" A view to show the details of a chosen product"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,

    }

    return render(request, 'products/product_detail.html', context)