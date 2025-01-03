from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F, Case, When, DecimalField, BooleanField, Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum

from .models import Product, PrimaryCategory, SpecialCategory
from .forms import ProductForm
from .utils import products_pagination

from reviews.models import Review
from reviews.forms import ReviewForm

from profiles.models import Wishlist


# Create your views here.

def all_products(request):
    """" A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    
    products = products.annotate(
        dynamic_price=Case(
            When(on_sale=True, then=F('sale_price')),
            default=F('price'),
            output_field=DecimalField(),
        )
    )
    query = None
    primary_categories = None
    special_categories = None
    sort = None
    direction = None
    wishlist_products = []
    current_primary_categories = None
    current_special_categories = None
    category_name = None
    special_category_name = None
    category_friendly_name = None
    special_category_friendly_name = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'price':
                sortkey = 'dynamic_price'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Handle filtering by primary category
        if 'primary_category' in request.GET:
            category_name = request.GET['primary_category']
            products = products.filter(primary_category__name__in=category_name.split(','))
            primary_categories = PrimaryCategory.objects.filter(name__in=category_name.split(','))
            # Fetch friendly name for display
            category_friendly_name = ', '.join(
                primary_categories.values_list('friendly_name', flat=True)
            )

        # Handle filtering by special category
        if 'special_category' in request.GET:
            special_category_name = request.GET['special_category']
            if special_category_name == "all_special_offers":
                # Show all products in special categories
                products = products.filter(special_categories__isnull=False).distinct()
            else:
                products = products.filter(special_categories__name=special_category_name)
                special_categories = SpecialCategory.objects.filter(name=special_category_name)
                # Fetch friendly name for display
                if special_categories.exists():
                    special_category_friendly_name = special_categories.first().friendly_name

        if 'deals' in request.GET:
            products = products.filter(on_sale=True)
            deals = True
            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn´t enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if not sort:
            products = products.order_by('name')
    
    
    current_sorting = f'{sort}_{direction}'
    
    reviews = Review.objects.all().filter()
    review_count = reviews.count()

    # Checking if the logged-in user has any products in their wishlist
    
    if request.user.is_authenticated:
        profile = request.user.userprofile
        # Fetch the wishlist items for the user
        wishlist_products = Wishlist.objects.filter(user=profile).values_list('product_id', flat=True)
        products = products.annotate(
            in_wishlist=Case(
                When(id__in=wishlist_products, then=True),
                default=False,
                output_field=BooleanField(),
            )
        )
    else:
        products = products.annotate(
            in_wishlist=Case(
                default=False,
                output_field=BooleanField(),
            )
        )

    # Count of products
    products_count = products.count()
    
    #Paginate Products
    products = products_pagination(request, products, 6)


    context = {
        'products': products,
        'products_count': products_count,
        'search_term' : query,
        'current_primary_categories': primary_categories,
        'current_special_categories': special_categories,
        'category_name': category_name,  
        'special_category_name': special_category_name,  
        'category_friendly_name': category_friendly_name,  
        'special_category_friendly_name': special_category_friendly_name,
        'current_sorting':  f'{sort}_{direction}',
        'review_count' : review_count,
        'wishlist_products' : wishlist_products,
        'special_categories': SpecialCategory.objects.all(),
    }

    return render(request, 'products/products.html', context)


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

    # reviews
    review_form = ReviewForm()
    reviews = Review.objects.all().filter(
        product=product).order_by('-created_on')
    review_count = reviews.count()  
    
    context = {
        'product': product,
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
