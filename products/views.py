from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum

from .models import ProductSize, Product, PrimaryCategory, SpecialCategory
from .forms import ProductForm

from reviews.models import Review
from reviews.forms import ReviewForm

from profiles.models import Wishlist

# Create your views here.

def all_products(request):
    """" A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    primary_categories = None
    special_categories = None
    sort = None
    direction = None
    deals = None
    new_arrivals = None
    wishlist_products = []

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey ='lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'primary_category' in request.GET:
            primary_categories = request.GET['primary_category'].split(',')
            products = products.filter(primary_category__name__in=primary_categories)
            primary_categories = PrimaryCategory.objects.filter(name__in=primary_categories)

        if 'special_category' in request.GET:
            special_categories = request.GET['special_category'].split(',')
            products = products.filter(special_category__name__in=special_categories)
            special_categories = SpecialCategory.objects.filter(name__in=special_categories)

        if 'deals' in request.GET:
            products = products.filter(on_sale=True)
            deals = True

        if 'new_arrivals' in request.GET:
            products = products[:8]
            new_arrivals = True
            
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
    
    reviews = Review.objects.all().filter()
    review_count = reviews.count()

    # Checking if the logged-in user has any products in their wishlist
    wishlist = False
    if request.user.is_authenticated:
        profile = request.user.userprofile
        # Fetch the wishlist items for the user
        wishlist_products = Wishlist.objects.filter(user=profile)
    

    context = {
        'products': products,
        'products_count': products_count,
        'search_term' : query,
        'current_primary_categories' : primary_categories,
        'current_special_categories' : speicial_categories,
        'current_sorting': current_sorting,
        'new_arrivals': new_arrivals,
        'deals': deals,
        'review_count' : review_count,
        'wishlist_products' : wishlist_products,
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

    wishlist = False
    user_review = None
    product = get_object_or_404(Product, pk=product_id)

    #Retrieve the user´s review if authenticated
    if request.user.is_authenticated:
        profile = request.user.userprofile
        user_review = Review.objects.filter(product=product, user=profile).first()
        if Wishlist.objects.filter(user=profile, product=product).exists():
            wishlist = True

    # Fetch size-specific stock data if the product has sizes
    sizes = product.sizes.all() if product.has_sizes else None

    # reviews
    review_form = ReviewForm()
    reviews = Review.objects.all().filter(
        product=product).order_by('-created_on')
    review_count = reviews.count()  
    
    context = {
        'product': product,
        'sizes' : sizes,
        'reviews': reviews,
        'wishlist': wishlist,
        'review_form' : review_form,
        'user_review' : user_review,
        'review_count' : review_count,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))