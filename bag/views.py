from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Choose the correct price based on sale status
    price = product.sale_price if product.on_sale and product.sale_price else product.price

    bag = request.session.get('bag', {})
    
    if size:
        # For products with sizes
        product_size = product.sizes.filter(size=size).first()
        if not product_size:
            messages.error(request, "Selected size is not available.")
            return redirect(redirect_url)

        current_quantity = bag.get(item_id, {}).get('items_by_size', {}).get(size, 0)
        
        if current_quantity + quantity > product_size.stock:
            messages.error(request, f"Only {product_size.stock - (current_quantity + quantity)} left in stock for size {size.upper()}!")
            return redirect(redirect_url)

         # Check if we're adding the last available stock
        if current_quantity + quantity == product_size.stock:
            messages.success(request, f"You're adding the last {product_size.stock} of size {size.upper()} {product.name} to your bag!")

        # Add to bag logic
        if item_id in bag:
            if size in bag[item_id]['items_by_size']:
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}

        # Decrement stock
        #product_size.stock -= quantity
        #product_size.save()

        messages.success(request, f"Added {quantity} of Size {size.upper()} {product.name} to your bag.")
    else:
        # For products without sizes
        current_quantity = bag.get(item_id, 0)

        if current_quantity + quantity > product.stock_amount:
            messages.error(request, f"Only {product.stock_amount - current_quantity} left in stock!")
            return redirect(redirect_url)

         # Check if we're adding the last available stock
        if current_quantity + quantity == product.stock_amount:
            messages.success(request, f"You're adding the last {product.stock_amount} of {product.name} to your bag!")
            
        # Add to bag logic
        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

        # Decrement stock
        #product.stock_amount -= quantity
        #product.save()

        messages.success(request, f"Added {quantity} of {product.name} to your bag.")
        
    request.session['bag'] = bag
    return redirect(redirect_url)
    

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    
     # Choose the correct price based on sale status
    price = product.sale_price if product.on_sale and product.sale_price else product.price
    print(price)

    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

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
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)