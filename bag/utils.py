def calculate_virtual_stock(product, bag):
    """
    Calculate the virtual stock of a product or
    its sizes based on the current bag contents.
    """
    if product.has_sizes:
        # Initialize size-based virtual stock
        virtual_stock = {size.size: size.stock for size in product.sizes.all()}

        if str(product.id) in bag and isinstance(bag[str(product.id)], dict):
            # Adjust size stock based on the quantities in the bag
            for size, quantity in bag[str(product.id)].get(
                'items_by_size', {}
            ).items():
                if size in virtual_stock:
                    virtual_stock[size] = max(
                        0, virtual_stock[size] - quantity)
    else:
        # Single stock amount for products without sizes
        virtual_stock = product.stock_amount
        if str(product.id) in bag and isinstance(bag[str(product.id)], int):
            virtual_stock = max(0, virtual_stock - bag[str(product.id)])

    return virtual_stock
