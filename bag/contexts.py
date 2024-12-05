from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .utils import calculate_virtual_stock

from products.models import Product


def bag_contents(request):
    '''
    Handles the shopping bag contents
    '''
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    items_to_remove = []
    discount = request.session.get('discount')
    discount_amount = 0

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        # remove items that are out of stock
        if product.in_stock is False:
            items_to_remove.append(item_id)

        total += product.product_price * int(quantity)
        product_count += int(quantity)
        bag_items.append({
            'item_id': item_id,
            'quantity': int(quantity),
            'product': product,
        })

    for item_id in items_to_remove:
        bag.pop(item_id)
        messages.error(request,
                       f'{item.title} is out of stock and has been removed')

    request.session['bag'] = bag

    # Apply discount to total amount excluding delivery
    if discount:
        discount_amount = (total * discount) / 100
        total -= discount_amount

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount_amount': discount_amount,
    }

    return context