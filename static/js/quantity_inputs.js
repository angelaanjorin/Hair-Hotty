document.addEventListener('DOMContentLoaded', function () {
    // Function to handle enabling/disabling of quantity buttons based on stock
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
        const selectedSize = document.getElementById('id_product_size').value;
        const stockList = document.querySelectorAll('#stock-list li');
        const stockDisplay = document.getElementById('stock-display');
        const addToBagButton = document.querySelector('input[type="submit"]');

        let stockAmount = 0;
        let sizeSelected = false;

        stockList.forEach(item => {
            const size = item.getAttribute('data-size');
            const stock = item.getAttribute('data-stock');

            if (size === selectedSize) {
                stockAmount = parseInt(stock, 10);
                sizeSelected = true;

                // Update stock display and button state
                if (stockAmount > 0) {
                    stockDisplay.innerHTML = `<span class="in-stock-label text-dark">IN STOCK: ${stockAmount}</span>`;
                    addToBagButton.disabled = false;  // Enable the button
                    addToBagButton.classList.remove("btn-not-allowed");
                    addToBagButton.classList.add("btn-cordovan");  // Change button color to cordovan
                } else {
                    stockDisplay.innerHTML = `<span class="out-of-stock-label text-dark">OUT OF STOCK</span>`;
                    addToBagButton.disabled = true;   // Disable the button
                    addToBagButton.classList.remove("btn-cordovan");
                    addToBagButton.classList.add("btn-not-allowed");  // Revert button color to disabled state
                }
            }
        });

        // If no size is selected, show the "Select a size" message
        if (!sizeSelected) {
            stockDisplay.innerHTML = `<span class="text-muted">Select a size to view stock.</span>`;
        }
    }

    // Validate input field directly
    $('.qty_input').on('input', function () {
        var itemId = $(this).data('item_id');
        var currentQuantity = parseInt($(this).val()) || 1; // Default to 1 if input is invalid
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
        } else if (currentQuantity < 1) {
            alert(`Quantity cannot be less than 1.`);
            $(this).val(1); // Reset to minimum allowed value
        }

        handleEnableDisable(itemId);
        updateStockDisplay(); // Update stock display based on quantity change
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
            alert(`You can only add up to ${stockAmount} items.`);
        }

        handleEnableDisable(itemId);
        updateStockDisplay(); // Update stock display after increment
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
        updateStockDisplay(); // Update stock display after decrement
    });

    // Attach the updateStockDisplay function to the 'onchange' event of the size dropdown
    const sizeDropdown = document.getElementById('id_product_size');
    if (sizeDropdown) {
        sizeDropdown.addEventListener('change', updateStockDisplay);
    }

    // Call the function once on page load to handle initial stock display
    updateStockDisplay();
});
