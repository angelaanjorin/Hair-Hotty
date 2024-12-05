from django.shortcuts import get_object_or_404

from products.models import Product


def validate_bag_stock(request):
    """
    Validates whether the stock in the bag is sufficient.
    It ensures the user's virtual stock does not exceed the actual available stock.
    """
    bag = request.session.get('bag', {})
    items_to_remove = []
    errors = []

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        # Check for products without sizes
        if isinstance(item_data, int):
            # Compare the virtual stock with real stock
            if product.stock_amount < item_data:
                items_to_remove.append(item_id)
                errors.append(f'Insufficient stock for {product.name}. Item removed.')
        else:
            # Check stock for products with sizes
            for size, quantity in item_data['items_by_size'].items():
                product_size = product.sizes.get(size=size)
                if product_size.stock < quantity:
                    items_to_remove.append(item_id)
                    errors.append(f'Insufficient stock for {product.name} (Size: {size}). Item removed.')

    return items_to_remove, errors