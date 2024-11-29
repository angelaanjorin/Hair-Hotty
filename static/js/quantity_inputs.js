// Disable +/- buttons outside 1-99 range and based on stock
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`.id_qty_${itemId}`).val());
    var stockAmount = 0;

    // Get selected size's stock amount
    var selectedSize = $('#id_product_size').val();
    $('#id_product_size option').each(function() {
        if ($(this).val() === selectedSize) {
            stockAmount = $(this).data('stock');
        }
    });

    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue >= stockAmount; // Disable increment if quantity >= stock
    $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Update stock display when size is selected
function updateStockDisplay() {
    var selectedSize = $('#id_product_size').val();
    var stockAmount = 0;

    $('#id_product_size option').each(function() {
        if ($(this).val() === selectedSize) {
            stockAmount = $(this).data('stock');
        }
    });

    // Update stock display
    $('#stock-display').text(`In stock: ${stockAmount}`);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    var currentQuantity = parseInt($(this).val());
    var stockAmount = 0;

    // Get selected size's stock amount
    var selectedSize = $('#id_product_size').val();
    $('#id_product_size option').each(function() {
        if ($(this).val() === selectedSize) {
            stockAmount = $(this).data('stock');
        }
    });

    // Validate quantity against stock
    if (currentQuantity > stockAmount) {
        alert(`Only ${stockAmount} items are available in stock.`);
        $(this).val(stockAmount); // Reset quantity to max stock
    }

    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentQuantity = parseInt($(closestInput).val());
    var stockAmount = 0;

    var selectedSize = $('#id_product_size').val();
    $('#id_product_size option').each(function() {
        if ($(this).val() === selectedSize) {
            stockAmount = $(this).data('stock');
        }
    });

    // Allow increment only if within stock limit
    if (currentQuantity < stockAmount) {
        $(closestInput).val(currentQuantity + 1);
    } else {
        showBootstrapToast(`You can only add up to ${stockAmount} items.`);
    }

    handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var itemId = $(this).data('item_id');
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentQuantity = parseInt($(closestInput).val());

    if (currentQuantity > 1) {
        $(closestInput).val(currentQuantity - 1);
    }

    handleEnableDisable(itemId);
});