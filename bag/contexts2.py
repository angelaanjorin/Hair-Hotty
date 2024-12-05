from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .utils import calculate_virtual_stock

from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    items_to_remove = []
    discount = request.session.get('discount')
    discount_amount = 0

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        # Calculate the virtual stock amount
        virtual_stock = calculate_virtual_stock(product, bag)

        if not product.in_stock:
            items_to_remove.append((item_id, f"{product.name} is out of stock."))
            continue

        price = product.sale_price if product.on_sale and product.sale_price else product.price

        if isinstance(item_data, int):
            # Product without sizes
            if isinstance(virtual_stock, int) and virtual_stock < item_data:
                items_to_remove.append((item_id, f"Insufficient stock for {product.name}."))
            else:
                total += item_data * price
                product_count += item_data
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'size': None,
                    'virtual_stock': virtual_stock,
                })
        elif isinstance(item_data, dict):
            # Product with sizes
            for size, quantity in item_data['items_by_size'].items():
                size_stock = virtual_stock.get(size, 0)
                if size_stock < quantity:
                    items_to_remove.append((item_id, f"Insufficient stock for {product.name} (Size: {size})."))
                else:
                    total += quantity * price
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                        'virtual_stock': size_stock,
                    })

    # Remove items after processing
    for item_id, message in items_to_remove:
        bag.pop(item_id, None)
        messages.error(request, message)

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