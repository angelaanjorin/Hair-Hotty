from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product

from discount.models import Discount


def view_bag(request):
    """ A view that renders the bag contents page """

    # Tells toast message which page user is on
    # To set toast bag summary button link
    context = {
        'on_bag_page': True
    }

    return render(request, 'bag/bag.html', context)
    

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    # Get the quantity from the request, default to 1 if not provided or invalid
    quantity = request.POST.get('quantity')
    if quantity:
        try:
            quantity = int(quantity)
        except ValueError:
            quantity = 1  # Default to 1 if quantity is not a valid integer
    else:
        quantity = 1  # Default to 1 if no quantity is provided

    redirect_url = request.POST.get('redirect_url', reverse('home'))  

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated Size {size.upper()} '
                                  f'{product.name} quantity to '
                                  f'{bag[item_id]["items_by_size"][size]}'))
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 (f'Added Size {size.upper()} '
                                  f'{product.name} to your bag'))
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             (f'Added Size {size.upper()} '
                              f'{product.name} to your bag'))
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'Updated Size {size.upper()} '
                              f'{product.name} quantity to '
                              f'{bag[item_id]["items_by_size"][size]}'))
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed Size {size.upper()} '
                              f'{product.name} from your bag'))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {bag[item_id]}'))
        else:
            bag.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request,
                             (f'Removed Size {size.upper()} '
                              f'{product.name} from your bag'))
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def add_discount(request):
    '''
    A view that handles applying
    discount codes
    '''
    if request.method == 'POST':
        code = request.POST.get('discount')
        try:
            code = Discount.objects.get(code__exact=code)
            if code.active:
                discount = code.discount
                request.session['discount'] = discount
                messages.success(request, 'Discount code applied successfully')
            else:
                messages.error(request, 'The code is not active')
        except ObjectDoesNotExist:
            messages.error(request, 'Invalid discount code.')
    return redirect('view_bag')


def remove_discount(request):
    '''
    A view that handles removing
    discount codes
    '''
    if 'discount' in request.session:
        try:
            del request.session['discount']
            messages.success(request, 'Discount code removed.')
        except KeyError:
            messages.error(request, 'Failed to remove discount code')
    else:
        messages.info(request, 'No discount code found')
    return redirect('view_bag')